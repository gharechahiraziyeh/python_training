#----------------------1------------------
def repeat(number, digit):
    count = 0
    while number > 0:
        if number % 10 == digit:
            count += 1
        number //= 10
    return count
number = int(input("number: "))
digit = int(input("digit: "))
print(digit, "repeat", repeat(number, digit), "times")
#-------------------------2-------------------
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def sum_fact(n):
    sum = 0
    for i in range(1, n + 1):
        sum += fact(i)
    return sum

number = int(input("number: "))
print("sum:", sum_fact(number))
#----------------------3--------------------
def max3(a, b, c):
    return max(a, b, c)

x = int(input("x: "))
y = int(input("y: "))
z = int(input("y: "))
print("Max: ", max3(x, y, z))