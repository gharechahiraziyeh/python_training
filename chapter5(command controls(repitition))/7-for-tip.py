# -----------1------------
l = ["a", "b", "c", "d"]
for i in range(0, len(l)):
    print(i, ":", l[i])
# ---------2--------------
print(list(enumerate(["a", "b", "c", "d"])))
# -----------3----------------
l = ["a", "b", "c", "d"]
for i, j in enumerate(l):
    print(i, ":", j)
# ----------4---------------
x = ["reza", "ali", "neda", "maryam"]
y = [20, 18, 25, 36]
for i, j in zip(x, y):
    print("name:", i, "age:", j)
# ------------5------------
x = ["ali", "reza", "neda", "sara"]
for i in reversed(x):
    print(i)
# ----------6------------
y = [20, 18, 25, 36]
for i in sorted(y):
    print(i)
# -------------7-------------
y = [20, 18, 25, 36]
for i in sorted(y, reverse=True):
    print(i)
