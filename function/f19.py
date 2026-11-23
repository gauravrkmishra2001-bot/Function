
def outer():
    print("Inside Outer..")
    def inner():
        print("Inside Inner..")
    return inner()

it=outer()