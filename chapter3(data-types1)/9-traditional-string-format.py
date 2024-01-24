# ---------------1------------------
x = 2
y = 3.6
print("x is: %i\ny is: %i\nz is: %i"%(x, y, 5 + 2))
# [(key)] [flag] [w] [.p] type
# ---------------2--------------------
print("%c" %(56))
print("%c" %('x'))
print("%s" %("reza"))
print("ali: %s" %("reza"))
print("%i" %(55))
print("%d" %(55))
print("%o" %(359))
print("%x" %(359))
print("%X" %(350674))
print("%e" %(350674))
print("%E" %(350674))
print("%f" %(1.2))
print("%F" %(2e+400))
print("%r" %("reza"))
# -----------------3--------------
y = 3.6732745632
print("%.2f" %(y))
print("%.8f" %(y))
print("%9.2f" %(y))
print("%+6.2f" %(y))
print("%0.6f" %(y))
# ------------4------------------
d = {"a" : 2, "b" : 7}
print("%(a)f\n%(b)i" %(d))
# -------------5------------------
x = 2
y = 3.6732745690
p = int(input("p:"))
z = int(input("z:"))
print("%8.*f" %(p, y))
print("%0*.*f" %(z,p, y))