# -----------1-------------
x = (1, 2, 3, "reza", [1, 2], (4, 5))
print(x)
print(type(x))
# ----------------2--------------
t = 1, 2, 3, 4
print(type(t))
print(t * 2)
print( 2 in t)
print(t[0:3:2])
# ----------------3------------------
t = (1, 2, [1, 2, 3], 4)
t[2][0] = 0
print(t)
print(len(t))
# ---------------4----------------
t = (1)
print(type(t))
# -------------5---------------
t = (1,)
print(type(t))
# --------------6-----------------
t = tuple("reza")
print(t)
print(type(t))
# ----------------7---------------
t = tuple()
print(type(t))
# --------------8---------------
t = (1, 2, 3)
l = list(t)
l[0] = 0
t = tuple(l)
print(t)
print(type(t))
# --------------9----------------
t = (1, 2, 3, 4, 5, 6)
x, y, *z = t
print(x)
print(y)
print(z)
# ------------10--------------
t = (1, 2, 3, 4, 5, 6)
x, *y, z = t
print(x)
print(y)
print(z)
# ------------11-------------
t = (1, 2, 3, 4, 5, 6)
*x, y, z = t
print(x)
print(y)
print(z)
# ------------12-------------
t1 = (1, 2, 3, [1, 2])
t2 = t1
print(id(t1))
print(id(t2))
t2[3][1] = 777
print(t1)
# -----------13----------
t1 = (1, 2, 3, [1, 2])
t2 = t1[:]
print(id(t1))
print(id(t2))
t2[3][1] = 777
print(t1)
# -------------14--------------
import copy
t1 = (1, 2, 3, [1, 2])
t2 = copy.copy(t1)
print(id(t1))
print(id(t2))
t2[3][1] = 777
print(t1)
# ---------------15------------
import copy
t1 = (1, 2, 3, [1, 2])
t2 = copy.deepcopy(t1)
print(id(t1))
print(id(t2))
t2[3][1] = 777
print(t1)