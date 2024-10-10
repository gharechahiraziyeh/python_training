#--------------------1-normal-----------
def func(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)

func(1, 2, 3)
#--------------------1-default-value-----------
def func(a=1, b=5, c=10):
    print("a=", a)
    print("b=", b)
    print("c=", c)

func(1, 2)
#--------------------3-default-value-----------
def func(a=1, b=5, c=10):
    print("a=", a)
    print("b=", b)
    print("c=", c)

func(b=0)
#---------------------4-normal+default-value---------------
def func(a, b, c=10):
    print("a=", a)
    print("b=", b)
    print("c=", c)

func(1, 2)
#---------------------5-normal+default-value---------------
def func(a, b, c=10):
    print("a=", a)
    print("b=", b)
    print("c=", c)

func(b=7, a=0)
#------------------6-*name----------------
def func(a, b, *c):
    print("a=", a)
    print("b=", b)
    print("c=", c)

func(1, 2, 3, 4, 5, 6)
#------------------7-*name----------------
def func(a, b, *c, d):
    print("a=", a)
    print("b=", b)
    print("c=", c)
    print("d=", d)

func(1, 2, 3, 4, 5, 6, d=0)
#-----------------------8-**name---------------
def func(**a):
    print("a=", a)


func(a=1, b=2, c=3)

#------------------9-**name-------------------
def func(a, **b):
    print("a=", a)
    print("b=", b)


func(a=1, b=2, c=3)
#----------------10-**name------------------
def func(a, b=0, *c, **d):
    print("a=", a)
    print("b=", b)
    print("c=", c)
    print("d=", d)

func(2, 3, 4, 6, 7, 8, c=0, d=9)
