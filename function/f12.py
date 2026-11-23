t=100

def f12():
    x=100
    print(f"Global variable is : {t}")
    print(f"local variable is : {x}")

f12()
#outside f12 x is not accesable
#print(x)
print(t)