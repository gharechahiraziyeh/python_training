# --------------1----------------
d = {"b": 5, "a": 10, "c": 20}
del d["b"]
print(d)
# --------------2---------------
d = {"b": 5, "a": 10, "c": 20}
d["c"] = "reza"
print(d)
# -----------3-----------
d = {"b": 5, "a": 10, "c": 20}
x = d["c"]
del d["c"]
d["x"] = x
print(d)
print(sorted(d.keys()))
print(sorted(d.values()))
print(sorted(d.values(), reverse= True))
print(d == {"b": 5, "a": 10, "c": 20})
# ----------4---------------
l = [1, 8, 0, 9, 2, 5]
print(sorted(l))
print(sorted(l, reverse= True))
# ------------5----------------
d = dict([("a", 5), ("b", 10), ("c", 25)])
print(d)
# -------------6---------------
d = dict(a=5, b=10, c=25)
print(d)
# -------------7------------
d = {x: x**2 for x in range(10)}
print(d)
# ------------8-------------
d = {
    "169": {"name": "reza", "age": 25},
    "172": {"name": "ali", "age": 14}
}
print(d["172"])
print(d["172"]["name"])
print(d["172"]["name"][0])
print(d["169"]["age"])
print(len(d))
# -------------9--------------
k = ["a", "b", "c"]
v = [1, 2, 3]
i = zip(k, v)
print(list(i))
d = dict(zip(k , v))
print(d)