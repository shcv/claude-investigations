---
id: msg-warning-372625
name: Warning Message
category: message
subcategory: warning
source_line: 372625
---

),
        q(Y, z)
      );
    };
  }
  async function HY2(A, K) {
    let q = new WjA.Root();
    if (((K = K || {}), K.includeDirs)) {
      if (!Array.isArray(K.includeDirs))
        return Promise.reject(Error("The includeDirs option must be an array"));
      Nc7(q, K.includeDirs);
    }
    let Y = await q.load(A, K);
    return (Y.resolveAll(), Y);
  }
  Tc7.loadProtosWithOptions = HY2;
  function JY2(A, K) {
    let q = new WjA.Root();
    if (((K = K || {}), K.includeDirs)) {
      if (!Array.isArray(K.includeDirs))
        throw Error("The includeDirs option must be an array");
      Nc7(q, K.includeDirs);
    }
    let Y = q.loadSync(A, K);
    return (Y.resolveAll(), Y);
  }
  Tc7.loadProtosWithOptionsSync = JY2;
  function OY2() {
    let A = jc7(),
      K = gk6(),
      q = Mc7(),
      Y = Pc7();
    (WjA.common("api", A.nested.google.nested.protobuf.nested),
      WjA.common("descriptor", K.nested.google.nested.protobuf.nested),
      WjA.common("source_context", q.nested.google.nested.protobuf.nested),
      WjA.common("type", Y.nested.google.nested.protobuf.nested));
  }
  Tc7.addCommonProtos = OY2;
});
var kc7 = v((_FA, Qk6) => {
  (function (A, K) {
    function q(Y) {
      return "default" in Y ? Y.default : Y;
    }
    if (typeof define === "function" && define.amd)
      define([], function () {
        var Y = {};
        return (K(Y), q(Y));
      });
    else if (typeof _FA === "object") {
      if ((K(_FA), typeof Qk6 === "object")) Qk6.exports = q(_FA);
    } else
      (function () {
        var Y = {};
        (K(Y), (A.Long = q(Y)));
      })();
  })(
    typeof globalThis < "u" ? globalThis : typeof self < "u" ? self : _FA,
    function (A) {
      (Object.defineProperty(A, "__esModule", { value: !0 }),
        (A.default = void 0));
      var K = null;
      try {
        K = new WebAssembly.Instance(
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
      function q(Q, u, d) {
        ((this.low = Q | 0), (this.high = u | 0), (this.unsigned = !!d));
      }
      (q.prototype.__isLong__,
        Object.defineProperty(q.prototype, "__isLong__", { value: !0 }));
      function Y(Q) {
        return (Q && Q.__isLong__) === !0;
      }
      function z(Q) {
        var u = Math.clz32(Q & -Q);
        return Q ? 31 - u : u;
      }
      q.isLong = Y;
      var w = {},
        H = {};
      function J(Q, u) {
        var d, r, c;
        if (u) {
          if (((Q >>>= 0), (c = 0 <= Q && Q < 256))) {
            if (((r = H[Q]), r)) return r;
          }
          if (((d = X(Q, 0, !0)), c)) H[Q] = d;
          return d;
        } else {
          if (((Q |= 0), (c = -128 <= Q && Q < 128))) {
            if (((r = w[Q]), r)) return r;
          }
          if (((d = X(Q, Q < 0 ? -1 : 0, !1)), c)) w[Q] = d;
          return d;
        }
      }
      q.fromInt = J;
      function O(Q, u) {
        if (isNaN(Q)) return u ? N : f;
        if (u) {
          if (Q < 0) return N;
          if (Q >= j) return y;
        } else {
          if (Q <= -M) return B;
          if (Q + 1 >= M) return x;
        }
        if (Q < 0) return O(-Q, u).neg();
        return X(Q % D | 0, (Q / D) | 0, u);
      }
      q.fromNumber = O;
      function X(Q, u, d) {
        return new q(Q, u, d);
      }
      q.fromBits = X;
      var $ = Math.pow;
      function _(Q, u, d) {
        if (Q.length === 0) throw Error("empty string");
        if (typeof u === "number") ((d = u), (u = !1));
        else u = !!u;
        if (
          Q === "NaN" ||
          Q === "Infinity" ||
          Q === "+Infinity" ||
          Q === "-Infinity"
        )
          return u ? N : f;
        if (((d = d || 10), d < 2 || 36 < d)) throw RangeError("radix");
        var r;
        if ((r = Q.indexOf("-")) > 0) throw Error("interior hyphen");
        else if (r === 0) return _(Q.substring(1), u, d).neg();
        var c = O($(d, 8)),
          YA = f;
        for (var e = 0; e < Q.length; e += 8) {
          var qA = Math.min(8, Q.length - e),
            HA = parseInt(Q.substring(e, e + qA), d);
          if (qA < 8) {
            var _A = O($(d, qA));
            YA = YA.mul(_A).add(O(HA));
          } else ((YA = YA.mul(c)), (YA = YA.add(O(HA))));
        }
        return ((YA.unsigned = u), YA);
      }
      q.fromString = _;
      function G(Q, u) {
        if (typeof Q === "number") return O(Q, u);
        if (typeof Q === "string") return _(Q, u);
        return X(Q.low, Q.high, typeof u === "boolean" ? u : Q.unsigned);
      }
      q.fromValue = G;
      var Z = 65536,
        W = 16777216,
        D = Z * Z,
        j = D * D,
        M = j / 2,
        P = J(W),
        f = J(0);
      q.ZERO = f;
      var N = J(0, !0);
      q.UZERO = N;
      var T = J(1);
      q.ONE = T;
      var C = J(1, !0);
      q.UONE = C;
      var R = J(-1);
      q.NEG_ONE = R;
      var x = X(-1, 2147483647, !1);
      q.MAX_VALUE = x;
      var y = X(-1, -1, !0);
      q.MAX_UNSIGNED_VALUE = y;
      var B = X(0, -2147483648, !1);
      q.MIN_VALUE = B;
      var b = q.prototype;
      if (
        ((b.toInt = function () {
          return this.unsigned ? this.low >>> 0 : this.low;
        }),
        (b.toNumber = function () {
          if (this.unsigned) return (this.high >>> 0) * D + (this.low >>> 0);
          return this.high * D + (this.low >>> 0);
        }),
        (b.toString = function (u) {
          if (((u = u || 10), u < 2 || 36 < u)) throw RangeError("radix");
          if (this.isZero()) return "0";
          if (this.isNegative())
            if (this.eq(B)) {
              var d = O(u),
                r = this.div(d),
                c = r.mul(d).sub(this);
              return r.toString(u) + c.toInt().toString(u);
            } else return "-" + this.neg().toString(u);
          var YA = O($(u, 6), this.unsigned),
            e = this,
            qA = "";
          while (!0) {
            var HA = e.div(YA),
              _A = e.sub(HA.mul(YA)).toInt() >>> 0,
              a = _A.toString(u);
            if (((e = HA), e.isZero())) return a + qA;
            else {
              while (a.length < 6) a = "0" + a;
              qA = "" + a + qA;
            }
          }
        }),
        (b.getHighBits = function () {
          return this.high;
        }),
        (b.getHighBitsUnsigned = function () {
          return this.high >>> 0;
        }),
        (b.getLowBits = function () {
          return this.low;
        }),
        (b.getLowBitsUnsigned = function () {
          return this.low >>> 0;
        }),
        (b.getNumBitsAbs = function () {
          if (this.isNegative())
            return this.eq(B) ? 64 : this.neg().getNumBitsAbs();
          var u = this.high != 0 ? this.high : this.low;
          for (var d = 31; d > 0; d--) if ((u & (1 << d)) != 0) break;
          return this.high != 0 ? d + 33 : d + 1;
        }),
        (b.isSafeInteger = function () {
          var u = this.high >> 21;
          if (!u) return !0;
          if (this.unsigned) return !1;
          return u === -1 && !(this.low === 0 && this.high === -2097152);
        }),
        (b.isZero = function () {
          return this.high === 0 && this.low === 0;
        }),
        (b.eqz = b.isZero),
        (b.isNegative = function () {
          return !this.unsigned && this.high < 0;
        }),
        (b.isPositive = function () {
          return this.unsigned || this.high >= 0;
        }),
        (b.isOdd = function () {
          return (this.low & 1) === 1;
        }),
        (b.isEven = function () {
          return (this.low & 1) === 0;
        }),
        (b.equals = function (u) {
          if (!Y(u)) u = G(u);
          if (
            this.unsigned !== u.unsigned &&
            this.high >>> 31 === 1 &&
            u.high >>> 31 === 1
          )
            return !1;
          return this.high === u.high && this.low === u.low;
        }),
        (b.eq = b.equals),
        (b.notEquals = function (u) {
          return !this.eq(u);
        }),
        (b.neq = b.notEquals),
        (b.ne = b.notEquals),
        (b.lessThan = function (u) {
          return this.comp(u) < 0;
        }),
        (b.lt = b.lessThan),
        (b.lessThanOrEqual = function (u) {
          return this.comp(u) <= 0;
        }),
        (b.lte = b.lessThanOrEqual),
        (b.le = b.lessThanOrEqual),
        (b.greaterThan = function (u) {
          return this.comp(u) > 0;
        }),
        (b.gt = b.greaterThan),
        (b.greaterThanOrEqual = function (u) {
          return this.comp(u) >= 0;
        }),
        (b.gte = b.greaterThanOrEqual),
        (b.ge = b.greaterThanOrEqual),
        (b.compare = function (u) {
          if (!Y(u)) u = G(u);
          if (this.eq(u)) return 0;
          var d = this.isNegative(),
            r = u.isNegative();
          if (d && !r) return -1;
          if (!d && r) return 1;
          if (!this.unsigned) return this.sub(u).isNegative() ? -1 : 1;
          return u.high >>> 0 > this.high >>> 0 ||
            (u.high === this.high && u.low >>> 0 > this.low >>> 0)
            ? -1
            : 1;
        }),
        (b.comp = b.compare),
        (b.negate = function () {
          if (!this.unsigned && this.eq(B)) return B;
          return this.not().add(T);
        }),
        (b.neg = b.negate),
        (b.add = function (u) {
          if (!Y(u)) u = G(u);
          var d = this.high >>> 16,
            r = this.high & 65535,
            c = this.low >>> 16,
            YA = this.low & 65535,
            e = u.high >>> 16,
            qA = u.high & 65535,
            HA = u.low >>> 16,
            _A = u.low & 65535,
            a = 0,
            JA = 0,
            jA = 0,
            MA = 0;
          return (
            (MA += YA + _A),
            (jA += MA >>> 16),
            (MA &= 65535),
            (jA += c + HA),
            (JA += jA >>> 16),
            (jA &= 65535),
            (JA += r + qA),
            (a += JA >>> 16),
            (JA &= 65535),
            (a += d + e),
            (a &= 65535),
            X((jA << 16) | MA, (a << 16) | JA, this.unsigned)
          );
        }),
        (b.subtract = function (u) {
          if (!Y(u)) u = G(u);
          return this.add(u.neg());
        }),
        (b.sub = b.subtract),
        (b.multiply = function (u) {
          if (this.isZero()) return this;
          if (!Y(u)) u = G(u);
          if (K) {
            var d = K.mul(this.low, this.high, u.low, u.high);
            return X(d, K.get_high(), this.unsigned);
          }
          if (u.isZero()) return this.unsigned ? N : f;
          if (this.eq(B)) return u.isOdd() ? B : f;
          if (u.eq(B)) return this.isOdd() ? B : f;
          if (this.isNegative())
            if (u.isNegative()) return this.neg().mul(u.neg());
            else return this.neg().mul(u).neg();
          else if (u.isNegative()) return this.mul(u.neg()).neg();
          if (this.lt(P) && u.lt(P))
            return O(this.toNumber() * u.toNumber(), this.unsigned);
          var r = this.high >>> 16,
            c = this.high & 65535,
            YA = this.low >>> 16,
            e = this.low & 65535,
            qA = u.high >>> 16,
            HA = u.high & 65535,
            _A = u.low >>> 16,
            a = u.low & 65535,
            JA = 0,
            jA = 0,
            MA = 0,
            hA = 0;
          return (
            (hA += e * a),
            (MA += hA >>> 16),
            (hA &= 65535),
            (MA += YA * a),
            (jA += MA >>> 16),
            (MA &= 65535),
            (MA += e * _A),
            (jA += MA >>> 16),
            (MA &= 65535),
            (jA += c * a),
            (JA += jA >>> 16),
            (jA &= 65535),
            (jA += YA * _A),
            (JA += jA >>> 16),
            (jA &= 65535),
            (jA += e * HA),
            (JA += jA >>> 16),
            (jA &= 65535),
            (JA += r * a + c * _A + YA * HA + e * qA),
            (JA &= 65535),
            X((MA << 16) | hA, (JA << 16) | jA, this.unsigned)
          );
        }),
        (b.mul = b.multiply),
        (b.divide = function (u) {
          if (!Y(u)) u = G(u);
          if (u.isZero()) throw Error("division by zero");
          if (K) {
            if (
              !this.unsigned &&
              this.high === -2147483648 &&
              u.low === -1 &&
              u.high === -1
            )
              return this;
            var d = (this.unsigned ? K.div_u : K.div_s)(
              this.low,
              this.high,
              u.low,
              u.high,
            );
            return X(d, K.get_high(), this.unsigned);
          }
          if (this.isZero()) return this.unsigned ? N : f;
          var r, c, YA;
          if (!this.unsigned) {
            if (this.eq(B))
              if (u.eq(T) || u.eq(R)) return B;
              else if (u.eq(B)) return T;
              else {
                var e = this.shr(1);
                if (((r = e.div(u).shl(1)), r.eq(f)))
                  return u.isNegative() ? T : R;
                else
                  return ((c = this.sub(u.mul(r))), (YA = r.add(c.div(u))), YA);
              }
            else if (u.eq(B)) return this.unsigned ? N : f;
            if (this.isNegative()) {
              if (u.isNegative()) return this.neg().div(u.neg());
              return this.neg().div(u).neg();
            } else if (u.isNegative()) return this.div(u.neg()).neg();
            YA = f;
          } else {
            if (!u.unsigned) u = u.toUnsigned();
            if (u.gt(this)) return N;
            if (u.gt(this.shru(1))) return C;
            YA = N;
          }
          c = this;
          while (c.gte(u)) {
            r = Math.max(1, Math.floor(c.toNumber() / u.toNumber()));
            var qA = Math.ceil(Math.log(r) / Math.LN2),
              HA = qA <= 48 ? 1 : $(2, qA - 48),
              _A = O(r),
              a = _A.mul(u);
            while (a.isNegative() || a.gt(c))
              ((r -= HA), (_A = O(r, this.unsigned)), (a = _A.mul(u)));
            if (_A.isZero()) _A = T;
            ((YA = YA.add(_A)), (c = c.sub(a)));
          }
          return YA;
        }),
        (b.div = b.divide),
        (b.modulo = function (u) {
          if (!Y(u)) u = G(u);
          if (K) {
            var d = (this.unsigned ? K.rem_u : K.rem_s)(
              this.low,
              this.high,
              u.low,
              u.high,
            );
            return X(d, K.get_high(), this.unsigned);
          }
          return this.sub(this.div(u).mul(u));
        }),
        (b.mod = b.modulo),
        (b.rem = b.modulo),
        (b.not = function () {
          return X(~this.low, ~this.high, this.unsigned);
        }),
        (b.countLeadingZeros = function () {
          return this.high ? Math.clz32(this.high) : Math.clz32(this.low) + 32;
        }),
        (b.clz = b.countLeadingZeros),
        (b.countTrailingZeros = function () {
          return this.low ? z(this.low) : z(this.high) + 32;
        }),
        (b.ctz = b.countTrailingZeros),
        (b.and = function (u) {
          if (!Y(u)) u = G(u);
          return X(this.low & u.low, this.high & u.high, this.unsigned);
        }),
        (b.or = function (u) {
          if (!Y(u)) u = G(u);
          return X(this.low | u.low, this.high | u.high, this.unsigned);
        }),
        (b.xor = function (u) {
          if (!Y(u)) u = G(u);
          return X(this.low ^ u.low, this.high ^ u.high, this.unsigned);
        }),
        (b.shiftLeft = function (u) {
          if (Y(u)) u = u.toInt();
          if ((u &= 63) === 0) return this;
          else if (u < 32)
            return X(
              this.low << u,
              (this.high << u) | (this.low >>> (32 - u)),
              this.unsigned,
            );
          else return X(0, this.low << (u - 32), this.unsigned);
        }),
        (b.shl = b.shiftLeft),
        (b.shiftRight = function (u) {
          if (Y(u)) u = u.toInt();
          if ((u &= 63) === 0) return this;
          else if (u < 32)
            return X(
              (this.low >>> u) | (this.high << (32 - u)),
              this.high >> u,
              this.unsigned,
            );
          else
            return X(
              this.high >> (u - 32),
              this.high >= 0 ? 0 : -1,
              this.unsigned,
            );
        }),
        (b.shr = b.shiftRight),
        (b.shiftRightUnsigned = function (u) {
          if (Y(u)) u = u.toInt();
          if ((u &= 63) === 0) return this;
          if (u < 32)
            return X(
              (this.low >>> u) | (this.high << (32 - u)),
              this.high >>> u,
              this.unsigned,
            );
          if (u === 32) return X(this.high, 0, this.unsigned);
          return X(this.high >>> (u - 32), 0, this.unsigned);
        }),
        (b.shru = b.shiftRightUnsigned),
        (b.shr_u = b.shiftRightUnsigned),
        (b.rotateLeft = function (u) {
          var d;
          if (Y(u)) u = u.toInt();
          if ((u &= 63) === 0) return this;
          if (u === 32) return X(this.high, this.low, this.unsigned);
          if (u < 32)
            return (
              (d = 32 - u),
              X(
                (this.low << u) | (this.high >>> d),
                (this.high << u) | (this.low >>> d),
                this.unsigned,
              )
            );
          return (
            (u -= 32),
            (d = 32 - u),
            X(
              (this.high << u) | (this.low >>> d),
              (this.low << u) | (this.high >>> d),
              this.unsigned,
            )
          );
        }),
        (b.rotl = b.rotateLeft),
        (b.rotateRight = function (u) {
          var d;
          if (Y(u)) u = u.toInt();
          if ((u &= 63) === 0) return this;
          if (u === 32) return X(this.high, this.low, this.unsigned);
          if (u < 32)
            return (
              (d = 32 - u),
              X(
                (this.high << d) | (this.low >>> u),
                (this.low << d) | (this.high >>> u),
                this.unsigned,
              )
            );
          return (
            (u -= 32),
            (d = 32 - u),
            X(
              (this.low << d) | (this.high >>> u),
              (this.high << d) | (this.low >>> u),
              this.unsigned,
            )
          );
        }),
        (b.rotr = b.rotateRight),
        (b.toSigned = function () {
          if (!this.unsigned) return this;
          return X(this.low, this.high, !1);
        }),
        (b.toUnsigned = function () {
          if (this.unsigned) return this;
          return X(this.low, this.high, !0);
        }),
        (b.toBytes = function (u) {
          return u ? this.toBytesLE() : this.toBytesBE();
        }),
        (b.toBytesLE = function () {
          var u = this.high,
            d = this.low;
          return [
            d & 255,
            (d >>> 8) & 255,
            (d >>> 16) & 255,
            d >>> 24,
            u & 255,
            (u >>> 8) & 255,
            (u >>> 16) & 255,
            u >>> 24,
          ];
        }),
        (b.toBytesBE = function () {
          var u = this.high,
            d = this.low;
          return [
            u >>> 24,
            (u >>> 16) & 255,
            (u >>> 8) & 255,
            u & 255,
            d >>> 24,
            (d >>> 16) & 255,
            (d >>> 8) & 255,
            d & 255,
          ];
        }),
        (q.fromBytes = function (u, d, r) {
          return r ? q.fromBytesLE(u, d) : q.fromBytesBE(u, d);
        }),
        (q.fromBytesLE = function (u, d) {
          return new q(
            u[0] | (u[1] << 8) | (u[2] << 16) | (u[3] << 24),
            u[4] | (u[5] << 8) | (u[6] << 16) | (u[7] << 24),
            d,
          );
        }),
        (q.fromBytesBE = function (u, d) {
          return new q(
            (u[4] << 24) | (u[5] << 16) | (u[6] << 8) | u[7],
            (u[0] << 24) | (u[1] << 16) | (u[2] << 8) | u[3],
            d,
          );
        }),
        typeof BigInt === "function")
      )
        ((q.fromBigInt = function (u, d) {
          var r = Number(BigInt.asIntN(32, u)),
            c = Number(BigInt.asIntN(32, u >> BigInt(32)));
          return X(r, c, d);
        }),
          (q.fromValue = function (u, d) {
            if (typeof u === "bigint") return fromBigInt(u, d);
            return G(u, d);
          }),
          (b.toBigInt = function () {
            var u = BigInt(this.low >>> 0),
              d = BigInt(this.unsigned ? this.high >>> 0 : this.high);
            return (d << BigInt(32)) | u;
          }));
      var F = (A.default = q);
    },
  );
});
var ik6 = v((Sc7) => {
  Object.defineProperty(Sc7, "__esModule", { value: !0 });
  Sc7.loadFileDescriptorSetFromObject =
    Sc7.loadFileDescriptorSetFromBuffer =
    Sc7.fromJSON =
    Sc7.loadSync =
    Sc7.load =
    Sc7.IdempotencyLevel =
    Sc7.isAnyExtension =
    Sc7.Long =
      void 0;
  var _Y2 = Od7(),
    uB = zj1(),
    ck6 = Dc7(),
    lk6 = Ec7(),
    GY2 = kc7();
  Sc7.Long = GY2;
  function ZY2(A) {
    return "@type" in A && typeof A["@type"] === "string";
  }
  Sc7.isAnyExtension = ZY2;
  var Lc7;
  (function (A) {
    ((A.IDEMPOTENCY_UNKNOWN = "IDEMPOTENCY_UNKNOWN"),
      (A.NO_SIDE_EFFECTS = "NO_SIDE_EFFECTS"),
      (A.IDEMPOTENT = "IDEMPOTENT"));
  })((Lc7 = Sc7.IdempotencyLevel || (Sc7.IdempotencyLevel = {})));
  var Rc7 = {
    longs: String,
    enums: String,
    bytes: String,
    defaults: !0,
    oneofs: !0,
    json: !0,
  };
  function WY2(A, K) {
    if (A === "") return K;
    else return A + "." + K;
  }
  function DY2(A) {
    return (
      A instanceof uB.Service || A instanceof uB.Type || A instanceof uB.Enum
    );
  }
  function jY2(A) {
    return A instanceof uB.Namespace || A instanceof uB.Root;
  }
  function yc7(A, K) {
    let q = WY2(K, A.name);
    if (DY2(A)) return [[q, A]];
    else if (jY2(A) && typeof A.nested < "u")
      return Object.keys(A.nested)
        .map((Y) => {
          return yc7(A.nested[Y], q);
        })
        .reduce((Y, z) => Y.concat(z), []);
    return [];
  }
  function Uk6(A, K) {
    return function (Y) {
      return A.toObject(A.decode(Y), K);
    };
  }
  function pk6(A) {
    return function (q) {
      if (Array.isArray(q))
        throw Error(
          
