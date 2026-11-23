
def f18():
    print("Inside f18..")

    def f181():
        print("Inside f181...")
        def f1811():
            print("Inside f1811")
        return f1811()
    return f181()

f18()
