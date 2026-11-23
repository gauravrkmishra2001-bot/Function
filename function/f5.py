# two a,b are positional 
# *d is variable length argument

def f5(a,b,*d,c):
    print(a)
    print(b)
    print(*d)
    print(c)

f5(10,20,30,40,c=50)
