# -----------1-------------
mark = int(input("mark: "))

if mark > 10:
    print("Accepted!")
    if 20 >= mark >= 15:
        print("A")
    elif 15 > mark > 10:
        print("B")
else:
    print("Rejected!")
# ---------------2---------------
y = 10
x = 10 + 2 if y < 20 else 5
print(x)
# -------------3------------------
# برنامه ای بنویسید که مشخص کند عدد وارد شده زوج هست یا فرد
x = int(input("x: "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
# ---------------4------------------
# برنامه ای بنویسید که عدد کوچکتر را بین دوعدد مشخص کند.
x = int(input("x: "))
y = int(input("y: "))
if x < y:
    print("min is x!")
else:
    print("min is y!")
# -----------5---------------
# برنامه ای بنویسید که 3 عدد را از کاربر بگیرد و کوچکترین آن را چاپ کند.
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

Min = x
if y < Min:
    Min = y
if z < Min:
    Min = z
print(Min)
