---
id: msg-warning-329556
name: Warning Message
category: message
subcategory: warning
source_line: 329556
---

),
        B(G, Z)
      );
    };
  }
  async function vB8(A, Q) {
    let B = new oZA.Root();
    if (((Q = Q || {}), Q.includeDirs)) {
      if (!Array.isArray(Q.includeDirs))
        return Promise.reject(Error("The includeDirs option must be an array"));
      JhB(B, Q.includeDirs);
    }
    let G = await B.load(A, Q);
    return (G.resolveAll(), G);
  }
  IhB.loadProtosWithOptions = vB8;
  function kB8(A, Q) {
    let B = new oZA.Root();
    if (((Q = Q || {}), Q.includeDirs)) {
      if (!Array.isArray(Q.includeDirs))
        throw Error("The includeDirs option must be an array");
      JhB(B, Q.includeDirs);
    }
    let G = B.loadSync(A, Q);
    return (G.resolveAll(), G);
  }
  IhB.loadProtosWithOptionsSync = kB8;
  function fB8() {
    let A = QhB(),
      Q = Ps1(),
      B = BhB(),
      G = GhB();
    (oZA.common("api", A.nested.google.nested.protobuf.nested),
      oZA.common("descriptor", Q.nested.google.nested.protobuf.nested),
      oZA.common("source_context", B.nested.google.nested.protobuf.nested),
      oZA.common("type", G.nested.google.nested.protobuf.nested));
  }
  IhB.addCommonProtos = fB8;
});
var KhB = w((WLA, xs1) => {
  (function (A, Q) {
    function B(G) {
      return "default" in G ? G.default : G;
    }
    if (typeof define === "function" && define.amd)
      define([], function () {
        var G = {};
        return (Q(G), B(G));
      });
    else if (typeof WLA === "object") {
      if ((Q(WLA), typeof xs1 === "object")) xs1.exports = B(WLA);
    } else
      (function () {
        var G = {};
        (Q(G), (A.Long = B(G)));
      })();
  })(
    typeof globalThis < "u" ? globalThis : typeof self < "u" ? self : WLA,
    function (A) {
      (Object.defineProperty(A, "__esModule", { value: !0 }),
        (A.default = void 0));
      var Q = null;
      try {
        Q = new WebAssembly.Instance(
          new WebAssembly.Module(
            new Uint8Array([
              0, 97, 115, 109, 1, 0, 0, 0, 1, 13, 2, 96, 0, 1, 127, 96, 4, 127,
              127, 127, 127, 1, 127, 3, 7, 6, 0, 1, 1, 1, 1, 1, 6, 6, 1, 127, 1,
              65, 0, 11, 7, 50, 6, 3, 109, 117, 108, 0, 1, 5, 100, 105, 118, 95,
              115, 0, 2, 5, 100, 105, 118, 95, 117, 0, 3, 5, 114, 101, 109, 95,
              115, 0, 4, 5, 114, 101, 109, 95, 117, 0, 5, 8, 103, 101, 116, 95,
              104, 105, 103, 104, 0, 0, 10, 191, 1, 6, 4, 0, 35, 0, 11, 36, 1,
              1, 126, 32, 0, 173, 32, 1, 173, 66, 32, 134, 132, 32, 2, 173, 32,
              3, 173, 66, 32, 134, 132, 126, 34, 4, 66, 32, 135, 167, 36, 0, 32,
              4, 167, 11, 36, 1, 1, 126, 32, 0, 173, 32, 1, 173, 66, 32, 134,
              132, 32, 2, 173, 32, 3, 173, 66, 32, 134, 132, 127, 34, 4, 66, 32,
              135, 167, 36, 0, 32, 4, 167, 11, 36, 1, 1, 126, 32, 0, 173, 32, 1,
              173, 66, 32, 134, 132, 32, 2, 173, 32, 3, 173, 66, 32, 134, 132,
              128, 34, 4, 66, 32, 135, 167, 36, 0, 32, 4, 167, 11, 36, 1, 1,
              126, 32, 0, 173, 32, 1, 173, 66, 32, 134, 132, 32, 2, 173, 32, 3,
              173, 66, 32, 134, 132, 129, 34, 4, 66, 32, 135, 167, 36, 0, 32, 4,
              167, 11, 36, 1, 1, 126, 32, 0, 173, 32, 1, 173, 66, 32, 134, 132,
              32, 2, 173, 32, 3, 173, 66, 32, 134, 132, 130, 34, 4, 66, 32, 135,
              167, 36, 0, 32, 4, 167, 11,
            ]),
          ),
          {},
        ).exports;
      } catch {}
      function B(p, k, c) {
        ((this.low = p | 0), (this.high = k | 0), (this.unsigned = !!c));
      }
      (B.prototype.__isLong__,
        Object.defineProperty(B.prototype, "__isLong__", { value: !0 }));
      function G(p) {
        return (p && p.__isLong__) === !0;
      }
      function Z(p) {
        var k = Math.clz32(p & -p);
        return p ? 31 - k : k;
      }
      B.isLong = G;
      var Y = {},
        J = {};
      function I(p, k) {
        var c, t, AA;
        if (k) {
          if (((p >>>= 0), (AA = 0 <= p && p < 256))) {
            if (((t = J[p]), t)) return t;
          }
          if (((c = W(p, 0, !0)), AA)) J[p] = c;
          return c;
        } else {
          if (((p |= 0), (AA = -128 <= p && p < 128))) {
            if (((t = Y[p]), t)) return t;
          }
          if (((c = W(p, p < 0 ? -1 : 0, !1)), AA)) Y[p] = c;
          return c;
        }
      }
      B.fromInt = I;
      function X(p, k) {
        if (isNaN(p)) return k ? L : M;
        if (k) {
          if (p < 0) return L;
          if (p >= C) return v;
        } else {
          if (p <= -$) return m;
          if (p + 1 >= $) return b;
        }
        if (p < 0) return X(-p, k).neg();
        return W(p % F | 0, (p / F) | 0, k);
      }
      B.fromNumber = X;
      function W(p, k, c) {
        return new B(p, k, c);
      }
      B.fromBits = W;
      var K = Math.pow;
      function V(p, k, c) {
        if (p.length === 0) throw Error("empty string");
        if (typeof k === "number") ((c = k), (k = !1));
        else k = !!k;
        if (
          p === "NaN" ||
          p === "Infinity" ||
          p === "+Infinity" ||
          p === "-Infinity"
        )
          return k ? L : M;
        if (((c = c || 10), c < 2 || 36 < c)) throw RangeError("radix");
        var t;
        if ((t = p.indexOf("-")) > 0) throw Error("interior hyphen");
        else if (t === 0) return V(p.substring(1), k, c).neg();
        var AA = X(K(c, 8)),
          VA = M;
        for (var OA = 0; OA < p.length; OA += 8) {
          var IA = Math.min(8, p.length - OA),
            PA = parseInt(p.substring(OA, OA + IA), c);
          if (IA < 8) {
            var kA = X(K(c, IA));
            VA = VA.mul(kA).add(X(PA));
          } else ((VA = VA.mul(AA)), (VA = VA.add(X(PA))));
        }
        return ((VA.unsigned = k), VA);
      }
      B.fromString = V;
      function E(p, k) {
        if (typeof p === "number") return X(p, k);
        if (typeof p === "string") return V(p, k);
        return W(p.low, p.high, typeof k === "boolean" ? k : p.unsigned);
      }
      B.fromValue = E;
      var D = 65536,
        H = 16777216,
        F = D * D,
        C = F * F,
        $ = C / 2,
        O = I(H),
        M = I(0);
      B.ZERO = M;
      var L = I(0, !0);
      B.UZERO = L;
      var _ = I(1);
      B.ONE = _;
      var T = I(1, !0);
      B.UONE = T;
      var x = I(-1);
      B.NEG_ONE = x;
      var b = W(-1, 2147483647, !1);
      B.MAX_VALUE = b;
      var v = W(-1, -1, !0);
      B.MAX_UNSIGNED_VALUE = v;
      var m = W(0, -2147483648, !1);
      B.MIN_VALUE = m;
      var u = B.prototype;
      if (
        ((u.toInt = function () {
          return this.unsigned ? this.low >>> 0 : this.low;
        }),
        (u.toNumber = function () {
          if (this.unsigned) return (this.high >>> 0) * F + (this.low >>> 0);
          return this.high * F + (this.low >>> 0);
        }),
        (u.toString = function (k) {
          if (((k = k || 10), k < 2 || 36 < k)) throw RangeError("radix");
          if (this.isZero()) return "0";
          if (this.isNegative())
            if (this.eq(m)) {
              var c = X(k),
                t = this.div(c),
                AA = t.mul(c).sub(this);
              return t.toString(k) + AA.toInt().toString(k);
            } else return "-" + this.neg().toString(k);
          var VA = X(K(k, 6), this.unsigned),
            OA = this,
            IA = "";
          while (!0) {
            var PA = OA.div(VA),
              kA = OA.sub(PA.mul(VA)).toInt() >>> 0,
              YA = kA.toString(k);
            if (((OA = PA), OA.isZero())) return YA + IA;
            else {
              while (YA.length < 6) YA = "0" + YA;
              IA = "" + YA + IA;
            }
          }
        }),
        (u.getHighBits = function () {
          return this.high;
        }),
        (u.getHighBitsUnsigned = function () {
          return this.high >>> 0;
        }),
        (u.getLowBits = function () {
          return this.low;
        }),
        (u.getLowBitsUnsigned = function () {
          return this.low >>> 0;
        }),
        (u.getNumBitsAbs = function () {
          if (this.isNegative())
            return this.eq(m) ? 64 : this.neg().getNumBitsAbs();
          var k = this.high != 0 ? this.high : this.low;
          for (var c = 31; c > 0; c--) if ((k & (1 << c)) != 0) break;
          return this.high != 0 ? c + 33 : c + 1;
        }),
        (u.isSafeInteger = function () {
          var k = this.high >> 21;
          if (!k) return !0;
          if (this.unsigned) return !1;
          return k === -1 && !(this.low === 0 && this.high === -2097152);
        }),
        (u.isZero = function () {
          return this.high === 0 && this.low === 0;
        }),
        (u.eqz = u.isZero),
        (u.isNegative = function () {
          return !this.unsigned && this.high < 0;
        }),
        (u.isPositive = function () {
          return this.unsigned || this.high >= 0;
        }),
        (u.isOdd = function () {
          return (this.low & 1) === 1;
        }),
        (u.isEven = function () {
          return (this.low & 1) === 0;
        }),
        (u.equals = function (k) {
          if (!G(k)) k = E(k);
          if (
            this.unsigned !== k.unsigned &&
            this.high >>> 31 === 1 &&
            k.high >>> 31 === 1
          )
            return !1;
          return this.high === k.high && this.low === k.low;
        }),
        (u.eq = u.equals),
        (u.notEquals = function (k) {
          return !this.eq(k);
        }),
        (u.neq = u.notEquals),
        (u.ne = u.notEquals),
        (u.lessThan = function (k) {
          return this.comp(k) < 0;
        }),
        (u.lt = u.lessThan),
        (u.lessThanOrEqual = function (k) {
          return this.comp(k) <= 0;
        }),
        (u.lte = u.lessThanOrEqual),
        (u.le = u.lessThanOrEqual),
        (u.greaterThan = function (k) {
          return this.comp(k) > 0;
        }),
        (u.gt = u.greaterThan),
        (u.greaterThanOrEqual = function (k) {
          return this.comp(k) >= 0;
        }),
        (u.gte = u.greaterThanOrEqual),
        (u.ge = u.greaterThanOrEqual),
        (u.compare = function (k) {
          if (!G(k)) k = E(k);
          if (this.eq(k)) return 0;
          var c = this.isNegative(),
            t = k.isNegative();
          if (c && !t) return -1;
          if (!c && t) return 1;
          if (!this.unsigned) return this.sub(k).isNegative() ? -1 : 1;
          return k.high >>> 0 > this.high >>> 0 ||
            (k.high === this.high && k.low >>> 0 > this.low >>> 0)
            ? -1
            : 1;
        }),
        (u.comp = u.compare),
        (u.negate = function () {
          if (!this.unsigned && this.eq(m)) return m;
          return this.not().add(_);
        }),
        (u.neg = u.negate),
        (u.add = function (k) {
          if (!G(k)) k = E(k);
          var c = this.high >>> 16,
            t = this.high & 65535,
            AA = this.low >>> 16,
            VA = this.low & 65535,
            OA = k.high >>> 16,
            IA = k.high & 65535,
            PA = k.low >>> 16,
            kA = k.low & 65535,
            YA = 0,
            ZA = 0,
            zA = 0,
            bA = 0;
          return (
            (bA += VA + kA),
            (zA += bA >>> 16),
            (bA &= 65535),
            (zA += AA + PA),
            (ZA += zA >>> 16),
            (zA &= 65535),
            (ZA += t + IA),
            (YA += ZA >>> 16),
            (ZA &= 65535),
            (YA += c + OA),
            (YA &= 65535),
            W((zA << 16) | bA, (YA << 16) | ZA, this.unsigned)
          );
        }),
        (u.subtract = function (k) {
          if (!G(k)) k = E(k);
          return this.add(k.neg());
        }),
        (u.sub = u.subtract),
        (u.multiply = function (k) {
          if (this.isZero()) return this;
          if (!G(k)) k = E(k);
          if (Q) {
            var c = Q.mul(this.low, this.high, k.low, k.high);
            return W(c, Q.get_high(), this.unsigned);
          }
          if (k.isZero()) return this.unsigned ? L : M;
          if (this.eq(m)) return k.isOdd() ? m : M;
          if (k.eq(m)) return this.isOdd() ? m : M;
          if (this.isNegative())
            if (k.isNegative()) return this.neg().mul(k.neg());
            else return this.neg().mul(k).neg();
          else if (k.isNegative()) return this.mul(k.neg()).neg();
          if (this.lt(O) && k.lt(O))
            return X(this.toNumber() * k.toNumber(), this.unsigned);
          var t = this.high >>> 16,
            AA = this.high & 65535,
            VA = this.low >>> 16,
            OA = this.low & 65535,
            IA = k.high >>> 16,
            PA = k.high & 65535,
            kA = k.low >>> 16,
            YA = k.low & 65535,
            ZA = 0,
            zA = 0,
            bA = 0,
            TA = 0;
          return (
            (TA += OA * YA),
            (bA += TA >>> 16),
            (TA &= 65535),
            (bA += VA * YA),
            (zA += bA >>> 16),
            (bA &= 65535),
            (bA += OA * kA),
            (zA += bA >>> 16),
            (bA &= 65535),
            (zA += AA * YA),
            (ZA += zA >>> 16),
            (zA &= 65535),
            (zA += VA * kA),
            (ZA += zA >>> 16),
            (zA &= 65535),
            (zA += OA * PA),
            (ZA += zA >>> 16),
            (zA &= 65535),
            (ZA += t * YA + AA * kA + VA * PA + OA * IA),
            (ZA &= 65535),
            W((bA << 16) | TA, (ZA << 16) | zA, this.unsigned)
          );
        }),
        (u.mul = u.multiply),
        (u.divide = function (k) {
          if (!G(k)) k = E(k);
          if (k.isZero()) throw Error("division by zero");
          if (Q) {
            if (
              !this.unsigned &&
              this.high === -2147483648 &&
              k.low === -1 &&
              k.high === -1
            )
              return this;
            var c = (this.unsigned ? Q.div_u : Q.div_s)(
              this.low,
              this.high,
              k.low,
              k.high,
            );
            return W(c, Q.get_high(), this.unsigned);
          }
          if (this.isZero()) return this.unsigned ? L : M;
          var t, AA, VA;
          if (!this.unsigned) {
            if (this.eq(m))
              if (k.eq(_) || k.eq(x)) return m;
              else if (k.eq(m)) return _;
              else {
                var OA = this.shr(1);
                if (((t = OA.div(k).shl(1)), t.eq(M)))
                  return k.isNegative() ? _ : x;
                else
                  return (
                    (AA = this.sub(k.mul(t))),
                    (VA = t.add(AA.div(k))),
                    VA
                  );
              }
            else if (k.eq(m)) return this.unsigned ? L : M;
            if (this.isNegative()) {
              if (k.isNegative()) return this.neg().div(k.neg());
              return this.neg().div(k).neg();
            } else if (k.isNegative()) return this.div(k.neg()).neg();
            VA = M;
          } else {
            if (!k.unsigned) k = k.toUnsigned();
            if (k.gt(this)) return L;
            if (k.gt(this.shru(1))) return T;
            VA = L;
          }
          AA = this;
          while (AA.gte(k)) {
            t = Math.max(1, Math.floor(AA.toNumber() / k.toNumber()));
            var IA = Math.ceil(Math.log(t) / Math.LN2),
              PA = IA <= 48 ? 1 : K(2, IA - 48),
              kA = X(t),
              YA = kA.mul(k);
            while (YA.isNegative() || YA.gt(AA))
              ((t -= PA), (kA = X(t, this.unsigned)), (YA = kA.mul(k)));
            if (kA.isZero()) kA = _;
            ((VA = VA.add(kA)), (AA = AA.sub(YA)));
          }
          return VA;
        }),
        (u.div = u.divide),
        (u.modulo = function (k) {
          if (!G(k)) k = E(k);
          if (Q) {
            var c = (this.unsigned ? Q.rem_u : Q.rem_s)(
              this.low,
              this.high,
              k.low,
              k.high,
            );
            return W(c, Q.get_high(), this.unsigned);
          }
          return this.sub(this.div(k).mul(k));
        }),
        (u.mod = u.modulo),
        (u.rem = u.modulo),
        (u.not = function () {
          return W(~this.low, ~this.high, this.unsigned);
        }),
        (u.countLeadingZeros = function () {
          return this.high ? Math.clz32(this.high) : Math.clz32(this.low) + 32;
        }),
        (u.clz = u.countLeadingZeros),
        (u.countTrailingZeros = function () {
          return this.low ? Z(this.low) : Z(this.high) + 32;
        }),
        (u.ctz = u.countTrailingZeros),
        (u.and = function (k) {
          if (!G(k)) k = E(k);
          return W(this.low & k.low, this.high & k.high, this.unsigned);
        }),
        (u.or = function (k) {
          if (!G(k)) k = E(k);
          return W(this.low | k.low, this.high | k.high, this.unsigned);
        }),
        (u.xor = function (k) {
          if (!G(k)) k = E(k);
          return W(this.low ^ k.low, this.high ^ k.high, this.unsigned);
        }),
        (u.shiftLeft = function (k) {
          if (G(k)) k = k.toInt();
          if ((k &= 63) === 0) return this;
          else if (k < 32)
            return W(
              this.low << k,
              (this.high << k) | (this.low >>> (32 - k)),
              this.unsigned,
            );
          else return W(0, this.low << (k - 32), this.unsigned);
        }),
        (u.shl = u.shiftLeft),
        (u.shiftRight = function (k) {
          if (G(k)) k = k.toInt();
          if ((k &= 63) === 0) return this;
          else if (k < 32)
            return W(
              (this.low >>> k) | (this.high << (32 - k)),
              this.high >> k,
              this.unsigned,
            );
          else
            return W(
              this.high >> (k - 32),
              this.high >= 0 ? 0 : -1,
              this.unsigned,
            );
        }),
        (u.shr = u.shiftRight),
        (u.shiftRightUnsigned = function (k) {
          if (G(k)) k = k.toInt();
          if ((k &= 63) === 0) return this;
          if (k < 32)
            return W(
              (this.low >>> k) | (this.high << (32 - k)),
              this.high >>> k,
              this.unsigned,
            );
          if (k === 32) return W(this.high, 0, this.unsigned);
          return W(this.high >>> (k - 32), 0, this.unsigned);
        }),
        (u.shru = u.shiftRightUnsigned),
        (u.shr_u = u.shiftRightUnsigned),
        (u.rotateLeft = function (k) {
          var c;
          if (G(k)) k = k.toInt();
          if ((k &= 63) === 0) return this;
          if (k === 32) return W(this.high, this.low, this.unsigned);
          if (k < 32)
            return (
              (c = 32 - k),
              W(
                (this.low << k) | (this.high >>> c),
                (this.high << k) | (this.low >>> c),
                this.unsigned,
              )
            );
          return (
            (k -= 32),
            (c = 32 - k),
            W(
              (this.high << k) | (this.low >>> c),
              (this.low << k) | (this.high >>> c),
              this.unsigned,
            )
          );
        }),
        (u.rotl = u.rotateLeft),
        (u.rotateRight = function (k) {
          var c;
          if (G(k)) k = k.toInt();
          if ((k &= 63) === 0) return this;
          if (k === 32) return W(this.high, this.low, this.unsigned);
          if (k < 32)
            return (
              (c = 32 - k),
              W(
                (this.high << c) | (this.low >>> k),
                (this.low << c) | (this.high >>> k),
                this.unsigned,
              )
            );
          return (
            (k -= 32),
            (c = 32 - k),
            W(
              (this.low << c) | (this.high >>> k),
              (this.high << c) | (this.low >>> k),
              this.unsigned,
            )
          );
        }),
        (u.rotr = u.rotateRight),
        (u.toSigned = function () {
          if (!this.unsigned) return this;
          return W(this.low, this.high, !1);
        }),
        (u.toUnsigned = function () {
          if (this.unsigned) return this;
          return W(this.low, this.high, !0);
        }),
        (u.toBytes = function (k) {
          return k ? this.toBytesLE() : this.toBytesBE();
        }),
        (u.toBytesLE = function () {
          var k = this.high,
            c = this.low;
          return [
            c & 255,
            (c >>> 8) & 255,
            (c >>> 16) & 255,
            c >>> 24,
            k & 255,
            (k >>> 8) & 255,
            (k >>> 16) & 255,
            k >>> 24,
          ];
        }),
        (u.toBytesBE = function () {
          var k = this.high,
            c = this.low;
          return [
            k >>> 24,
            (k >>> 16) & 255,
            (k >>> 8) & 255,
            k & 255,
            c >>> 24,
            (c >>> 16) & 255,
            (c >>> 8) & 255,
            c & 255,
          ];
        }),
        (B.fromBytes = function (k, c, t) {
          return t ? B.fromBytesLE(k, c) : B.fromBytesBE(k, c);
        }),
        (B.fromBytesLE = function (k, c) {
          return new B(
            k[0] | (k[1] << 8) | (k[2] << 16) | (k[3] << 24),
            k[4] | (k[5] << 8) | (k[6] << 16) | (k[7] << 24),
            c,
          );
        }),
        (B.fromBytesBE = function (k, c) {
          return new B(
            (k[4] << 24) | (k[5] << 16) | (k[6] << 8) | k[7],
            (k[0] << 24) | (k[1] << 16) | (k[2] << 8) | k[3],
            c,
          );
        }),
        typeof BigInt === "function")
      )
        ((B.fromBigInt = function (k, c) {
          var t = Number(BigInt.asIntN(32, k)),
            AA = Number(BigInt.asIntN(32, k >> BigInt(32)));
          return W(t, AA, c);
        }),
          (B.fromValue = function (k, c) {
            if (typeof k === "bigint") return fromBigInt(k, c);
            return E(k, c);
          }),
          (u.toBigInt = function () {
            var k = BigInt(this.low >>> 0),
              c = BigInt(this.unsigned ? this.high >>> 0 : this.high);
            return (c << BigInt(32)) | k;
          }));
      var e = (A.default = B);
    },
  );
});
var hs1 = w((ChB) => {
  Object.defineProperty(ChB, "__esModule", { value: !0 });
  ChB.loadFileDescriptorSetFromObject =
    ChB.loadFileDescriptorSetFromBuffer =
    ChB.fromJSON =
    ChB.loadSync =
    ChB.load =
    ChB.IdempotencyLevel =
    ChB.isAnyExtension =
    ChB.Long =
      void 0;
  var gB8 = nfB(),
    hx = $11(),
    fs1 = AhB(),
    bs1 = WhB(),
    uB8 = KhB();
  ChB.Long = uB8;
  function mB8(A) {
    return "@type" in A && typeof A["@type"] === "string";
  }
  ChB.isAnyExtension = mB8;
  var EhB;
  (function (A) {
    ((A.IDEMPOTENCY_UNKNOWN = "IDEMPOTENCY_UNKNOWN"),
      (A.NO_SIDE_EFFECTS = "NO_SIDE_EFFECTS"),
      (A.IDEMPOTENT = "IDEMPOTENT"));
  })((EhB = ChB.IdempotencyLevel || (ChB.IdempotencyLevel = {})));
  var DhB = {
    longs: String,
    enums: String,
    bytes: String,
    defaults: !0,
    oneofs: !0,
    json: !0,
  };
  function dB8(A, Q) {
    if (A === "") return Q;
    else return A + "." + Q;
  }
  function cB8(A) {
    return (
      A instanceof hx.Service || A instanceof hx.Type || A instanceof hx.Enum
    );
  }
  function pB8(A) {
    return A instanceof hx.Namespace || A instanceof hx.Root;
  }
  function HhB(A, Q) {
    let B = dB8(Q, A.name);
    if (cB8(A)) return [[B, A]];
    else if (pB8(A) && typeof A.nested < "u")
      return Object.keys(A.nested)
        .map((G) => {
          return HhB(A.nested[G], B);
        })
        .reduce((G, Z) => G.concat(Z), []);
    return [];
  }
  function ys1(A, Q) {
    return function (G) {
      return A.toObject(A.decode(G), Q);
    };
  }
  function vs1(A) {
    return function (B) {
      if (Array.isArray(B))
        throw Error(
          
