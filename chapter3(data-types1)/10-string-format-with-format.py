# ------------1--------------------
x = 5
y = 7.55445732
print("x is {}\ny is {}\nz is {}".format(5, y, 5 + 7))
print("x is {0}\ny is {1}\nz is {2}".format(5, y, 5 + 7))
print("x is {0}\ny is {1}\nz is {1}".format(5, y, 5 + 7))
print("x is {2}\ny is {0}\nz is {1}".format(5, y, 5 + 7))
# ------------------2---------------------
d = {"x": 5, "y": 8, "z": 2.366}
print("x is {x}\ny is {y}\nz is {z}".format(**d))
print("x is {y}\ny is {z}\nz is {z}".format(**d))
print("x is {x}\ny is {y}\nz is {z}".format(x = d["x"], y = d["y"], z = d["z"]))
print("x is {2}\ny is {1}\nz is {0}".format(*"rez"))
print("x is {2}\ny is {1}\nz is {0}".format(*[1, 2, 9]))
# -----------------3--------------------
# "{"[field_name] ["!" conversion] [":" format_spec ] "}"
print("x is {}".format(5))
print("x is {0!s}".format("reza"))
print("x is {0!r}".format("reza"))
print("x is {0!a}".format("reza"))
print("x is {:.2}".format(1.5644))
# -----------------4--------------------
# [[fill]align][sign][#][0][width][grouping_option][.percision][type]
print("x is {0:c}".format(110))
print("x is {0:d}".format(110))
print("x is {0:%}".format(1.25))
print("x is {0:.2f}".format(4.36456))
print("x is {0:,.2f}".format(4345689214))
print("x is {0:_.2f}".format(4345689214))
print("x is {0:20,.2f}".format(4345689214))
print("x is {0:020,.2f}".format(4345689214))
print("x is {:#b}".format(23456))
print("x is {:#o}".format(23456))
print("x is {:#x}".format(23456))
print("x is {:+}".format(52))
print("x is {:<15}".format(12))
print("x is {:<15}".format(12), "*", sep="")
print("x is {:>15}".format(12), "*", sep="")
print("x is {:^15}".format(12), "*", sep="")
print("x is {:*<15}".format(12), "*", sep="")
print("x is {:{align}15}".format(12, align = "<"), "*", sep="")
print("x is {:{align}{sign}15}".format(12, align = "<", sign = "+"), "*", sep="")
# ------------------5---------------
x = input("sign: ")
print("x is {:{align}{sign}15}".format(12, align = "<", sign = x), "*", sep="")