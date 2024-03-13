# ---------1-------------
list1 = [1, 2, 3, 4, 5, 6]
for i in list1:
    print(i)
# ----------2---------
str1 = "reza dolati"
for s in str1:
    print(s)
# ----------3--------
t = ("a", "b", "c")
for i in t:
    print(i)
# -----------4----------
d = {"A": 1, "B": 2, "C": 3}
for i in d:
    print(i)
# ------------5----------
list1 = [67, 92, 102, 150, 87, 72, 110]
for c in list1:
    print(chr(c))
# ----------6-----------
list1 = [67, 92, 102, 150, 87, 72, 110]
for c in list1:
    if chr(c) == "f":
        break
    print(chr(c))
else:
    print("OK!")
# --------------7-------------
list1 = [67, 92, 102, 150, 87, 72, 110]
for c in list1:
    if chr(c) == "f":
        continue
    print(chr(c))
else:
    print("OK!")
# ----------8-----------
list1 = [1, 2, 8, 9, 6, 7, 3, 6]
list2 = [14, 10, 8, 3, 7, 9, 1, 0, 20]
for i in list1:
    for j in list2:
        if i == j:
            print(i)
# ---------------9---------------
for a, b, c in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
    print(a, b, c)
# -------------10-----------
d = {"A": 1, "B": 2, "C": 3}
for key, value in d.items():
    print(key, ":", value)

