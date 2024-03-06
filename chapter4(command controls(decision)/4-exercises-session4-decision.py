# یک عدد از کاربر بگیرید و بررسی کنید آیا هم بر 2 و هم بر 5 بخش پذیر هست یا نه؟
x = int(input("x: "))
if x % 2 == 0 and x % 5 == 0:
    print("Yes!")
else:
    print("No!")

# اضلاع یک مثلث را از کاربر گرفته و مشخص کنید که آیا این اضلاع تشکیل مثلث می دهد یا خیر؟ اگر جواب مثبت هست ه نوع
# مثلثی؟ (متساوی الاضلاع یا متساوی الساقین یا مختلف الاضلاع یا قائم الزاویه)
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a + b > c and a + c > a and b + c > a:
    print("It is a triangle")
    if c ** 2 == a ** 2 + b ** 2 or a ** 2 == c ** 2 + b ** 2 or b ** 2 == a ** 2 + c ** 2:
        print("It is ghaemozaviye")
    if a == b == c:
        print("It is motasaviolazlae")
    if a == b or b == c or c == a:
        print("It is motasaviosaghein")
    if a != b and b != c and a != c:
        print("It is mokhtalefolazlae")
else:
    print("It is not a triangle")

# یک کارکتر از کاربر بگیرید و مشخص کنید کارکتر وارد شده عدد هست ، حروف انگلیسی هست یا سایر نمادها
ch = input("Enter a character: ")
if 48 <= ord(ch) <= 57:
    print("Your character is number.")
elif 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
    print("Your character is letter.")
else:
    print("Other!")
