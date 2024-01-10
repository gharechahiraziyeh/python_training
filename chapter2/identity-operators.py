# ---------1--------
x = 5
y = 5
print(x is y)
# --------2----------
x = [1, 2, 4]
print(id(x))
y = [1, 2, 4]
print(id(y))
print(x is y)
print(x is not y)
z = x
print(x is z)