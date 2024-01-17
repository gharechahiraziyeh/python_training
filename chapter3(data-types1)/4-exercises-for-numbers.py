# 1-برنامه ای بنویسید که شعاع دایره را از کاربر گرفته و محیط و مساحت دایره را حساب کند
r = int(input("Enter r: "))
mohit = 2 * 3.14 * r
masahat = 3.14 * (r ** 2)
print("mohit= ", mohit)
print("masahat= ", masahat)
# 2-برنامه ای بنویسید که یک عدد را از کاربر گرفته و مربع و مکعب آن را چاپ کند
x = int(input("Enter x: "))
x2 = x ** 2
x3 = x** 3
print(x, "^", 2, "=", x2)
print(x, "^", 3, "=", x3)
# 3-برنامه ای بنویسید که دو عدد را از کاربر گرفته اولی را به توان دومی برساند و نتیجه را چاپ کند
x = int(input("Enter x: "))
y = int(input("Enter y: "))
xy = x ** y
print(x, "^", y, "=", xy)
# 4-برنامه ای بنویسید که سه عدد را گرفته میانگین آنها را محاسبه و نتیجه را چاپ کند
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
ave = (x + y + z) / 3
print("Average= ", ave)

