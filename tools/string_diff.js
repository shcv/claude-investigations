#!/usr/bin/env node
/**
 * AST-based string extraction and comparison for JavaScript files.
 *
 * Uses Acorn parser to accurately extract all string literals, then
 * performs set-based comparison to find actual changes.
 *
 * Usage:
 *   node string_diff.js extract <file.js> [--filter] [--normalize]
 *   node string_diff.js compare <old_version> <new_version> [--filter]
 *   node string_diff.js diff <old.js> <new.js> [--filter]
 *
 * Examples:
 *   node string_diff.js compare 2.1.14 2.1.15 --filter
 *   node string_diff.js extract cli.js --filter --normalize
 */

const fs = require('fs');
const path = require('path');

let acorn;
let walk;

try {
  acorn = require('acorn');
  walk = require('acorn-walk');
} catch (e) {
  console.error('Error: acorn and acorn-walk are required.');
  console.error('Install with: npm install acorn acorn-walk');
  process.exit(1);
}

/**
 * Extract all string literals from JavaScript code using AST parsing.
 */
function extractStrings(code) {
  const strings = new Set();

  try {
    const ast = acorn.parse(code, {
      ecmaVersion: 'latest',
      sourceType: 'module',
      allowHashBang: true,
      allowReserved: true,
      onComment: () => {},
    });

    walk.simple(ast, {
      Literal(node) {
        if (typeof node.value === 'string') {
          strings.add(node.value);
        }
      },
      TemplateLiteral(node) {
        // Extract the quasi (static parts) of template literals
        for (const quasi of node.quasis) {
          if (quasi.value.cooked) {
            strings.add(quasi.value.cooked);
          }
        }
      },
    });
  } catch (e) {
    console.error(`Parse error: ${e.message}`);
    process.exit(1);
  }

  return strings;
}

/**
 * Normalize a string for comparison.
 */
function normalizeString(s) {
  // Collapse whitespace
  return s.replace(/\s+/g, ' ').trim();
}

/**
 * Check if string is likely noise (code fragment, identifier, etc.)
 */
function isNoise(s) {
  // Too short
  if (s.length < 10) return true;

  // Too long - likely embedded data
  if (s.length > 500) return true;

  // Starts with code characters
  if (/^[)\]};,=+&|<>]/.test(s)) return true;

  // Pure identifiers (camelCase, snake_case, CONSTANT_CASE, kebab-case)
  if (/^[a-z][a-zA-Z0-9]*$/.test(s) && s.length < 25) return true;
  if (/^[a-z][a-z0-9]*(_[a-z0-9]+)+$/.test(s)) return true;
  if (/^[A-Z][A-Z0-9_]+$/.test(s) && s.length < 25) return true;
  if (/^[a-z][a-z0-9]*(-[a-z0-9]+)+$/.test(s) && s.length < 30) return true;

  // Code patterns at start
  const codeStarts = [
    'return ', 'throw ', 'if(', 'if (', 'else', 'case ',
    'function ', 'const ', 'let ', 'var ', 'class ',
    'import ', 'export ', 'switch ', 'for ', 'while ',
    'try ', 'catch ', 'new ', 'typeof ', 'instanceof ',
  ];
  for (const cs of codeStarts) {
    if (s.startsWith(cs)) return true;
  }

  // Contains obvious code patterns
  if (/\bfunction\s*\(/.test(s)) return true;
  if (/=>\s*\{/.test(s)) return true;
  if (/\bcase\s+['"]/.test(s)) return true;
  if (/\breturn\s+\{/.test(s)) return true;

  // Object literal patterns
  if (/:\s*['"][^'"]+['"],\s*\w+:/.test(s)) return true;

  // High code punctuation ratio
  const codePunct = (s.match(/[(){}[\];=><&|!?:]/g) || []).length;
  if (s.length > 0 && codePunct / s.length > 0.15) return true;

  // Multiple colons followed by quotes (object literal)
  const colonQuotes = (s.match(/:\s*['"]/g) || []).length;
  if (colonQuotes >= 3) return true;

  return false;
}

/**
 * Process extracted strings with optional filtering and normalization.
 */
function processStrings(strings, options = {}) {
  const result = new Set();

  for (let s of strings) {
    if (options.normalize) {
      s = normalizeString(s);
    }

    if (!s) continue;
    if (options.filter && isNoise(s)) continue;

    result.add(s);
  }

  // Sort using byte order (consistent across platforms)
  return [...result].sort((a, b) => {
    if (a < b) return -1;
    if (a > b) return 1;
    return 0;
  });
}

/**
 * Find the JS file for a version in the archive.
 */
function findVersionFile(version) {
  const scriptDir = path.dirname(__filename);
  const archiveDir = path.join(scriptDir, '..', 'archive', 'claude-code');

  const pretty = path.join(archiveDir, 'pretty', `pretty-v${version}.js`);
  if (fs.existsSync(pretty)) return pretty;

  const original = path.join(archiveDir, 'original', `cli-v${version}.js`);
  if (fs.existsSync(original)) return original;

  return null;
}

/**
 * Extract command - extract strings from a file.
 */
function cmdExtract(filePath, options) {
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    process.exit(1);
  }

  const code = fs.readFileSync(filePath, 'utf-8');
  const rawStrings = extractStrings(code);
  const strings = processStrings(rawStrings, options);

  for (const s of strings) {
    // Escape newlines for line-based output
    console.log(s.replace(/\n/g, '\\n'));
  }

  console.error(`Total: ${strings.length} strings`);
}

/**
 * Compare two sets of strings and return added/removed.
 */
function compareStringSets(oldStrings, newStrings) {
  const oldSet = new Set(oldStrings);
  const newSet = new Set(newStrings);

  const added = newStrings.filter(s => !oldSet.has(s));
  const removed = oldStrings.filter(s => !newSet.has(s));
  const common = oldStrings.filter(s => newSet.has(s));

  return { added, removed, common };
}

/**
 * Diff command - compare strings between two files.
 */
function cmdDiff(oldPath, newPath, options) {
  if (!fs.existsSync(oldPath)) {
    console.error(`File not found: ${oldPath}`);
    process.exit(1);
  }
  if (!fs.existsSync(newPath)) {
    console.error(`File not found: ${newPath}`);
    process.exit(1);
  }

  const oldCode = fs.readFileSync(oldPath, 'utf-8');
  const newCode = fs.readFileSync(newPath, 'utf-8');

  const oldStrings = processStrings(extractStrings(oldCode), options);
  const newStrings = processStrings(extractStrings(newCode), options);

  console.error(`Old: ${oldStrings.length} strings`);
  console.error(`New: ${newStrings.length} strings`);

  const { added, removed, common } = compareStringSets(oldStrings, newStrings);

  console.error(`Common: ${common.length}`);
  console.error(`Added: ${added.length}`);
  console.error(`Removed: ${removed.length}`);
  console.error('');

  if (added.length > 0) {
    console.log('=== ADDED ===');
    for (const s of added) {
      // Truncate for display, escape newlines
      const display = s.length > 200 ? s.slice(0, 200) + '...' : s;
      console.log(`+ ${display.replace(/\n/g, '\\n')}`);
    }
  }

  if (removed.length > 0) {
    console.log('\n=== REMOVED ===');
    for (const s of removed) {
      const display = s.length > 200 ? s.slice(0, 200) + '...' : s;
      console.log(`- ${display.replace(/\n/g, '\\n')}`);
    }
  }

  // Return counts for programmatic use
  return { added: added.length, removed: removed.length, common: common.length };
}

/**
 * Compare command - compare two versions from the archive.
 */
function cmdCompare(oldVersion, newVersion, options) {
  const oldPath = findVersionFile(oldVersion);
  const newPath = findVersionFile(newVersion);

  if (!oldPath) {
    console.error(`Version ${oldVersion} not found in archive`);
    process.exit(1);
  }
  if (!newPath) {
    console.error(`Version ${newVersion} not found in archive`);
    process.exit(1);
  }

  console.error(`Comparing v${oldVersion} -> v${newVersion}`);
  return cmdDiff(oldPath, newPath, options);
}

/**
 * Parse command line arguments.
 */
function parseArgs(args) {
  const options = {
    filter: false,
    normalize: false,
  };

  const positional = [];

  for (const arg of args) {
    if (arg === '--filter') {
      options.filter = true;
    } else if (arg === '--normalize') {
      options.normalize = true;
    } else if (!arg.startsWith('--')) {
      positional.push(arg);
    }
  }

  return { options, positional };
}

/**
 * Print usage information.
 */
function printUsage() {
  console.log(`Usage:
  node string_diff.js extract <file.js> [--filter] [--normalize]
  node string_diff.js compare <old_version> <new_version> [--filter]
  node string_diff.js diff <old.js> <new.js> [--filter]

Options:
  --filter     Filter out noise (short strings, identifiers, code fragments)
  --normalize  Collapse whitespace in strings

Examples:
  node string_diff.js compare 2.1.14 2.1.15 --filter
  node string_diff.js extract pretty.js --filter --normalize
  node string_diff.js diff old.js new.js --filter`);
}

// Main
const args = process.argv.slice(2);
const { options, positional } = parseArgs(args);

if (positional.length === 0) {
  printUsage();
  process.exit(1);
}

const command = positional[0];

switch (command) {
  case 'extract':
    if (positional.length < 2) {
      console.error('Usage: string_diff.js extract <file.js> [--filter] [--normalize]');
      process.exit(1);
    }
    // Always normalize for extract
    options.normalize = true;
    cmdExtract(positional[1], options);
    break;

  case 'compare':
    if (positional.length < 3) {
      console.error('Usage: string_diff.js compare <old_version> <new_version> [--filter]');
      process.exit(1);
    }
    // Always normalize for comparison
    options.normalize = true;
    cmdCompare(positional[1], positional[2], options);
    break;

  case 'diff':
    if (positional.length < 3) {
      console.error('Usage: string_diff.js diff <old.js> <new.js> [--filter]');
      process.exit(1);
    }
    // Always normalize for comparison
    options.normalize = true;
    cmdDiff(positional[1], positional[2], options);
    break;

  default:
    console.error(`Unknown command: ${command}`);
    printUsage();
    process.exit(1);
}
