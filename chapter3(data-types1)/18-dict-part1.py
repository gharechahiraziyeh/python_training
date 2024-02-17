# ------------1---------------
d = {}
print(d)
print(type(d))
# -------------2-------------
d = {"a": 5, "b": 10}
print(d["a"])
# ------------3-----------
d = {(1, 2): 5, "b": [1, 2, 3], 1: 15}
print(d[(1, 2)])
print(d["b"])
# -----------4------------------
d = {"a": 5, "b":10, "a": 8}
print(d)
# ------------5---------------
d = {"a": 5, "b": 10}
d["a"] = 20
d["c"] = 30
print(d)
print(d.keys())
print(list(d.keys()))
print(d.values())
print(list(d.values()))
print(d.items())
print(list(d.items()))