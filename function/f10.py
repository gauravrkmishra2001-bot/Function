#Here, b is a default parameter (default argument),
#but its default value is overridden by the value passed during the function call.

def f10(a,b=20):
    print(a)
    print(b)

f10(100,30)