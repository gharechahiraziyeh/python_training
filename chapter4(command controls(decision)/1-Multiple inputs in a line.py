# ----------1--------------
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
print(30 * "-")
print("x =", x, "\ny =", y, "\nz =", z)
# -----------2---------------
x, y, z = 5, 8, 9

print(30 * "-")
print("x =", x, "\ny =", y, "\nz =", z)
# ------------3-----------------
x, y, z = input("x,y,z: ").split(",")

print(30 * "-")
print("x =", x, "\ny =", y, "\nz =", z)
# -------------4-----------------
x = input("Enter a list: ").split(",")

print(30 * "-")
print(x)
# --------------5--------------
l = [int(x) for x in input("Enter a list: ").split(",")]

print(30 * "-")
print(l)


