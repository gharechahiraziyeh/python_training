# ------------1-------------------
s = "hi, how are you, reza is a bad boy"
c = input("Enter a char: ")
print(s.count(c))
# ---------------------2---------------
s = input("enter string: ")
s = s.rstrip()
i = s.rfind(" ")
print(s[i + 1:])
# ------------------3------------------
s1 = input("enter string1: ")
s2 = input("enter string2: ")
print(s2 in s1)
# ---------------------4---------------
s = input("enter string: ")
print(s.replace(" ", "").replace("\t", ""))
# --------------------5-------------------
phone = input("Enter number: ")
print(phone.lstrip("0"))