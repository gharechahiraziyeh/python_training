# --------------1--------------
mark = int(input("mark: "))
if mark < 10:
    print("Rejected!")
else:
    print("Accepted!")
print("\n***End***")
# -----------2---------------
mark = int(input("mark: "))
if 20 >= mark >= 15:
    print("A")
elif 15 > mark >= 10:
    print("B")
elif 10 > mark >= 5:
    print("C")
elif 5 > mark >=0:
    print("D")
else:
    print("Wrong!")
print("\n***End***")
