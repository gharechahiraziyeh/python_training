# -----------1---------------
x = 0b1010111
print(x)
print(type(x))
# -----------2--------------
x = 0o72367
print(x)
print(type(x))
# -----------3-------------
x = 0x12f6e2a
print(x)
print(type(x))
# ---------------4-------------
x = 10
print(bin(x))
print(oct(x))
print(hex(x))
print(type(x))
# ------------5---------------
x = 1
x = float(x)
print(x)
print(type(x))
# -----------6---------------
x = 1.9
x = int(x)
print(x)
print(type(x))
# ------------7-------------
x = 1
x = complex(x)
print(x)
print(type(x))
# ------------8-------------
x = "12"
x = int(x)
print(x)
print(type(x))
# -------------9----------------
x = 12366.564
x = str(x)
print(x)
print(type(x))
# ------------10-----------------
f = 0.1 + 0.2
print(f)
# ----------11-------------------
from decimal import Decimal
x = float(Decimal("0.1") + Decimal("0.2"))
print(x)
print(x == 0.3)
print(type(x))
# ------------12-----------------
from fractions import Fraction
print(Fraction(0.5))
# ---------------13------------
x = 1_000_000_000_000
print(x)
print(type(x))
# --------------14----------
f = 1e+5
print(f)
# ---------------15------------
f = 1e+400
print(f)
# --------------16---------------
f = float("inf")
print(f)
print(type(f))
# -------------17-----------------
f = -2e+500
print(f)
# -------------18----------------
c = 1 + 3j
print(c.real)
print(c.imag)
print(c.conjugate)
print(type(c))
# ----------------19-------------
c = 1+ 3j
d = 1 - 3j
print(c + d)
print(c - d)
print(c * d)
print(c / d)
# ----------------20----------------
x = 3.2545645
print(round(x, 2))
# --------------21-------------
x = -3.2545546
print(abs(x))
# -------------22-----------
x = 3
print(pow(x, 3))
