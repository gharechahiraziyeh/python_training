def func(a, b, /, c, *, d, e):
    print("a=", a)
    print("b=", b)
    print("c=", c)
    print("d=", d)
    print("e=", e)


func(1, 2, 3, d=4, e=5)