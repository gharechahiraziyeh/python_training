#-------------------1----------------
def func(x):
    print(x * 2)

y = func
y(6)
#---------------2-----------------
def A(a):
    print(a)

    def B(b):
        print(b ** 2)
    B(a)

A(5)
print(A.__name__)
#-------------3----------------
def descending(mylist):
    print(sorted(mylist))

def ascending(mylist):
    print(sorted(mylist , reverse=True))

def mysort(f, mylist):
    f(mylist)

mysort(ascending, [1,4,8,2,1,0,9])
#-----------------4---------------------
def mysort(s):

    def ascending(x):
        print(sorted(x))

    def descending(x):
        print(sorted(x, reverse=True))

    if s == "a":
        return ascending
    elif s == "d":
        return descending

action = input("action:")
func = mysort(action)
func([4, 7, 6, 9, 0, 3, 1, 2])