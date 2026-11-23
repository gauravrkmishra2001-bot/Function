

def f17():
    print("f17 called..")
    def f171():
        print("Inside f171")
    return f171()

inner=f17()

#inner call f171() from inside it
