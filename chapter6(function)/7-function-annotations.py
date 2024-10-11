#------------------1-----------------
def func(x:int, y:int, z:int):
    print("x:", x)
    print("y:", y)
    print("z:", z)

func(1, 2, 3)
#---------------------2-----------------
def func(x:int, y:int, z:int) -> int:
    return x + y + z

func(1, 2, 3)
#-----------------3---------------------
def func(x:int, y:int, z:int) -> tuple:
    return (x + y + z, y , z)

print(func(1, 2, 3))
#---------------4------------
def func(x:"reza", y:int, z:int) -> tuple:
    return (x + y + z, y, z)

print(func.__annotations__)
#--------------5-------------
def func(x:int=1, y:int=2, z:int=3) -> tuple:
    return (x + y + z, y, z)

print(func())
