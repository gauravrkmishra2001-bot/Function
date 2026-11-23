


x=400
def f15():
    global x
    x=500
    print("Inside :",x)
def f152():
    print("Inside :",x)

print("outside before call :",x)
f15()