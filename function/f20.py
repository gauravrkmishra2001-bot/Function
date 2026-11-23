
def f1(l):
    def f2(w):
        def f3(h):
            return l*w*h
        return f3
    return f2

#print(f1(1)(2)(3))

fun=f1(1)(2)

print(fun(3))
print(fun.__closure__)
for cell in fun.__closure__:
    print(cell.cell_contents)