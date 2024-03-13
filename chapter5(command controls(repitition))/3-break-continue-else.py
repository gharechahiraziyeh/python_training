# -----------1--------------
i = 1
while i <= 100:
    print(i)
    if i == 5:
        break
    i += 1
# -----------2-----------
n = float(input("n: "))
m = n
while True:
    s = input("Do you continue? ")
    if s.lower() == "no":
        break
    n = float(input("n: "))
    if n < m:
        m = n
print(m, "is smallest number!")
# --------------3-------------
i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print(i)
else:
    print("OK!")
# -------------4------------
n = int(input("n: "))
i = 2
if n > 1:
    while i < (n // 2) + 1:
        if n % i == 0:
            print(n, "is not a prime number!")
            break
        i += 1
    else:
        print(n, "is a prime number!")
else:
    print(n, "is not a prime number!")

