
x=100
def f1():
    x=200
    print(f"Inside :",x)
def f2():
    print(f"Inside :{x}")

f1()
f2()
print(f"Outside : {x}")