# ------------1-----------------
l1 = [1, 2, 3]
l2 = l1
print(id(l1))
print(id(l2))
l2[0] = 0
print(l2)
print(id(l1))
print(id(l2))
# ------------2-----------
l1 = [1, 2, 3]
l2 = l1[:]
print(id(l1))
print(id(l2))
l2[0] = 0
print(l2)
print(id(l1))
print(id(l2))
# -------------3---------------
l1 = [1, 2, 3]
l2 = l1.copy()
print(id(l1))
print(id(l2))
l2[0] = 0
print(l2)
print(id(l1))
print(id(l2))
# ---------------4-----------
x = [1, 2, ['a', 'b', [1.1, 2.2]]]
print(x)
print(x[2])
print(x[2][0])
print(x[2][1])
print(x[2][2][0])