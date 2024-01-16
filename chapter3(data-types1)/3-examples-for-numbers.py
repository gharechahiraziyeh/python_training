# 1-برنامه ای بنویسید که وزن را بر اساس کیلو گرم دریافت می کند و بر اساس گرم چاپ می کند
kg = int(input("Enter kg: "))
g = kg * 1000
print("g = ", g, "g", sep="")
# 2-برنامه ای بنویسید که مساحت مثلث را محاسبه کند
x = int(input("Enter x: "))
y = int(input("Enter y: "))
s = 0.5 * x * y
print("s= ", s)
# 3-برنامه ای بنویسید که یک ماشین حساب ساده طراحی کند و جمع و ضرب و تفریق و تقسیم دو عدد را انجام دهد
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(x, "+", y, "=", x + y)
print(x, "-", y, "=", x - y)
print(x, "*", y, "=", x * y)
print(x, "/", y, "=", x / y)
# 4-برنامه ای بنویسید که یک عدد سه رقمی را از کاربر دریافت کند و ارقام آن را چاپ کند
x = int(input("Enter x: "))
temp = x % 10
print(temp)
x = x // 10
temp = x % 10
print(temp)
x = x // 10
temp = x % 10
print(temp)
# 5-برنامه ای بنویسید که زاویه بر حسب درجه دریافت کند و به رادیان نمایش دهد
D = int(input("Enter D: "))
R = D * (3.14 / 180)
print("R = ", R)