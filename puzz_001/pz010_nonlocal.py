def myfunc1():
    x = "A"

    def myfunc2():
        nonlocal x
        x = "B"

    myfunc2()
    return x


print(myfunc1())
