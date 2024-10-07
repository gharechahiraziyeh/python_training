#-------------1-------------
def cube(x):
    return x ** 3
y = int(input("y: "))
print(cube(y))
#-------------2--------------
def cube():
    x = int(input("x: "))
    return x ** 3
n = cube()
print(n)
#----------------3-----------
def cube():
    x = int(input("x: "))
    print(x ** 3)
cube()