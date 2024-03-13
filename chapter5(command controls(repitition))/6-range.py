# ---------1---------
for i in range(10):
    print(i)
# ------------2----------
for i in range(2, 10):
    print(i)
# -----------3-------------
for i in range(2, 10, 2):
    print(i)
# -----------4-----------
for i in range(-20, -150, -20):
    print(i)
# ----------5------------
l = input("names: ").split("-")
for i in range(0, len(l)):
    print(i, l[i])
# --------6--------------
n = int(input("n: "))
m = 1
for i in range(1, n + 1):
    m *= i
print("f: ", m)
# ------------7-----------
n = input("n: ")
s = ""
for i in range(len(n) - 1, -1, -1):
    s += n[i]
x = int(s)
print(type(x))
print(s)
# ------------8---------
n = int(input("n: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
