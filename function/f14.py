#how to use global inside function

x=100
def f14():
    global x
    x+=10
    print("Inside after :",x)

print(f"outside before call ",x)
f14()
print("outside after call :",x)