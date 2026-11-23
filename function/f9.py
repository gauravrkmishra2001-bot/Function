

def f9(a,*b,**c):
    print(a)
    print(*b)
    print(c)

f9(10,30,40,c=60,b=70,d=50)