def decorator1(func):
    def do_something():
        print("I'm decorator1")
        func()

    return do_something


@decorator1
def func1():
    print("I'm func1")


func1()
