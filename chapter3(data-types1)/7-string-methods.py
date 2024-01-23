# ----------1-----------------
s = "re$#@&*(z a"
print(len(s))
print(s[0:len(s)])
# -----------2----------------
s = "reza"
print(s.upper())
# ------------3------------------
s = "rEZa"
print(s.lower())
# -------------4-----------------
s = "reza dolati"
print(s.count("a"))
print(s.endswith("i"))
print(s.endswith("ati"))
print(s.startswith("r"))
print(s.find("r"))
print(s.rfind("a"))
# -------------5------------------
s = "reza5"
print(s.isalnum())
print(s.isnumeric())
# --------------6-------------------
s = "*"
l = ["A", "B", "8"]
print(s.join(l))
# ---------------7-----------------
s = "reza,dolati,01,python"
print(s.split(","))
# ------------8----------------
s = "reza dolati 01 python"
print(s.replace(" ", "+"))
# ------------9-----------------
s = "      reza dolati 01 python        "
print(s.strip(" "))
print(s.lstrip(" "))
print(s.rstrip(" "))
# ----------------10-----------------
s = "reza dolati"
print(s.capitalize())