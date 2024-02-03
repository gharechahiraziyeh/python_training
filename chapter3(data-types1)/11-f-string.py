# -----------1-------------------
x = 5
y = 4.6353
print(f"x is {x}\ny is {y}\nz is {5 ** 2}")
# -----------------2----------------
x = "reza"
y = 4.6353
print(f"x is {x!r}\ny is {y}\nz is {5**2}")
# --------------3------------------
x = 3.5646
y = 4.6353
print(f"x is {x:010.2f}\ny is {y}\nz is {5 ** 2}")
# ------------------4----------------
x = 3.5646
y = 4.6353
print(f"{{x}} is {x}")
# -------------------5-----------------
x = 3.5646
y = 4.6353
print(f"{{x}} is {{{x}}}")
# ------------------6----------------
x = "reza"
def f(s):
    return s.upper()
print(f"x is {f(x)}")
print(f"x is {x.replace('a', '-')}")
# -----------------7--------------------
name = "reza"
age = 38
msg = (
    f"name: {name}\n"
    f"age: {age}\n"
)
print(msg)
# ----------------8-----------------
import datetime
print(datetime.datetime.now())
print(datetime.datetime.today())
today = datetime.datetime.today()
print(f"{today:%Y}")
print(f"{today:%Y/%m}")
print(f"{today:%Y/%B}")
print(f"{today:%Y/%B %H}")
print(f"{today:%Y/%B %H:%M}")
# -------------------9-----------------
x = 5
print(f"{x:+>15}*")
print(f"{x:-<15}*")