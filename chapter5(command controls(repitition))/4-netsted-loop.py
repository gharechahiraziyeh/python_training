# ---------1----------
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print("\t", j)
        j += 1
    print(i)
    i += 1
# ------------2---------------
l = input("name: ").split("-")
i = 0
while i < len(l):
    s = l[i]
    j = 0
    while j < len(s):
        if j % 2 == 0:
            print(s[j].upper(), end="")
        else:
            print(s[j], end="")
        j += 1
    print()
    i += 1
# ----------3------------
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(i * j, "\t")
        j += 1
    print()
    i += 1
# ------------4---------------
n = int(input("n: "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1


