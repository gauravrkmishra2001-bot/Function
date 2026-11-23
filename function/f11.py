
def f11(a,b,/,c=10,*arg,d,**r):
    print(a)
    print(b)
    print(c)
    print(arg)
    print(d)
    print(r)

f11(10,20,30,40,50,60,d=70,id=101,name="gourav")