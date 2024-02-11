# ------------1-----------------
daneshjoo = [1, 5, 9, "reza"]
print(daneshjoo, "\n", type(daneshjoo))
number = list("reza")
print(number, "\n", type(number))
s = "a l i m o"
ch = s.split(" ")
print(ch, "\n", type(ch))
# ---------------2----------------
l = [1, 5, 9, "reza"]
print(l[0])
print(l[3])
print(l[:])
print(l[1:3])
print(l[::2])
l2 = l * 2
print(l2)
print(l + ["a", "b"])
# ------------3--------------
l = [1, 5, 9, "reza"]
l[1] = 10
print(l)
# ------------4--------------
l = [1, 5, 9, "reza"]
z = [1, 5, 9, "reza"]
print(l == z)
# -------------5--------------
l = [1, 5, 9, "reza"]
z = [1, 9, 5, "reza"]
print(l == z)
print(1 in l)
print("reza" in l)