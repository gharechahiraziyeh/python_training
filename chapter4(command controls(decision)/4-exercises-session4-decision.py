# یک عدد از کاربر بگیرید و بررسی کنید آیا هم بر 2 و هم بر 5 بخش پذیر هست یا نه؟
x = int(input("x: "))
if x % 2 == 0 and x % 5 == 0:
    print("Yes!")
else:
    print("No!")
