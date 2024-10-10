#-------------1-normal--------------
def max3(a, b, c):
    print(max(a, b , c))

max3(4, 3, 1)
#----------------2-name=value---------
def max3(a, b, c):
    print(max(a, b , c))

max3(a=4, b=3, c=1)
#----------------3-name=value------------
def max3(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)

max3(c=4, a=8, b=1)
#--------------4-normal+name=value-------------
def max3(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)

max3(4, c=8, b=1)
#--------------5-normal+name=value-------------
def max3(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)

max3(4, 8, c=1)
#-------------------6-*iterable-------------
def max3(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)

max3(*[4, 8, 5])
#-------------------7-*iterable-------------
def max3(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)

x = [4, 8, 5]
max3(*x)
#-------------------8-*iterable-------------
def max3(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)

x = {4, 8, 5}
max3(*x)
#-------------------9-*iterable-------------
def max3(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)

x = (4, 8, 5)
max3(*x)
#-------------------10-*iterable-------------
def max3(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)

x = "123"
max3(*x)
#-------------------11-------------
def max3(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)


max3([1, 2, 3], 8, 0)
#-------------------12-**dict-------------
def max3(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)

d = {"a": 1, "b":8, "c": 6}
max3(**d)
