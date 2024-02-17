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
# ------------5------------------
x = [1, 2, ['reza', 'dolati'], 3]
print(x[2][1][0])
print(x[2][1][-1])
# -----------6----------------
l1 = [1, 2, ["a", "b"]]
l2 = l1.copy()
print(id(l1))
print(id(l2))
l2[2][0] = 0
print(l1)
print(l2)
print(id(l1))
print(id(l2))
# --------------7---------
import copy
l1 = [1, 2, ["a", "b"]]
l2 = copy.copy(l1)
print(id(l1))
print(id(l2))
l2[2][0] = 0
print(l1)
print(l2)
print(id(l1))
print(id(l2))
# ------------------8---------------
import copy
l1 = [1, 2, ["a", "b"]]
l2 = copy.deepcopy(l1)
print(id(l1))
print(id(l2))
l2[2][0] = 0
print(l1)
print(l2)
print(id(l1))
print(id(l2))
