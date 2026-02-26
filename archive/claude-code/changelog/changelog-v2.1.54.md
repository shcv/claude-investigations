# Changelog for version 2.1.54


## Summary

This is a targeted patch release that fixes file handling on Windows. Three separate file-open operations now use portable string mode flags instead of POSIX numeric constants, resolving potential issues with command output logging and task output on Windows.

## Bug Fixes

- **Fixed file open operations on Windows for bash command output**: The bash command runner now opens its output log file using the portable string flag `"w"` (write) on Windows, instead of the bitwise POSIX flags `O_WRONLY | O_CREAT | O_TRUNC`, which may not behave correctly on Windows. Non-Windows platforms continue to use the POSIX flags with `O_NOFOLLOW` for symlink safety. (search for `process.platform === "win32"` in `pj1` at line ~269290)

- **Fixed file open operations on Windows for task output appending**: The task output writer class now opens files using the portable string flag `"a"` (append) on Windows, instead of the bitwise POSIX flags `O_WRONLY | O_APPEND | O_CREAT`. Previously, there was no Windows-specific handling in this code path. (search for `process.platform === "win32"` in class `z31` at line ~130992)

- **Fixed file open operations on Windows for task output creation**: The task output file creation function now uses the portable string flag `"wx"` (exclusive write) on Windows, instead of the bitwise POSIX flags `O_WRONLY | O_CREAT | O_EXCL`. This ensures exclusive-create semantics work correctly on Windows. (search for `process.platform === "win32"` in `bq8` at line ~131075)
