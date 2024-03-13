# -----------1------------
n = int(input("n: "))
while n < 100:
    if n % 2 == 0:
        print(n)
    n += 1
# ----------2-----------------
n = 1
while n < 1000:
    if n % 3 == 0 and n % 7 == 0:
        print(n)
    n += 1
# ------------3-------------
row = 1
n = int(input("rows: "))
while row <= n:
    print("*" * row)
    row += 1
# -----------4------------
row = int(input("rows: "))
while row >= 1:
    print("*" * row)
    row -= 1
# --------5-----------
n = int(input("Enter a number: "))
i = 1
while i <= n:
    if n % i == 0:
        print(i, end=" ")
    i += 1
# ------------6---------------
n = int(input("Enter a number: "))
i = 1
c = 0
while i < n:
    if n % i == 0:
        c += i
    i += 1
if c == n:
    print("complete!")
else:
    print("No!")
# -----------7----------
i = 1
a, b = 0, 1
while i <= 20:
    print(a)
    a, b = b, a + b
    i += 1

