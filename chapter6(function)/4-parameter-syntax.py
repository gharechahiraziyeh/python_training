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