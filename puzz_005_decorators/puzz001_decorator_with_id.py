"""
id() function in Python. In Python, id() function is a built-in function that returns the unique identifier of
an object. The identifier is an integer, which represents the memory address of the object. The id() function is
commonly used to check if two variables or objects refer to the same memory location.
"""


def decorator1(func):
    def do_something():
        print(f"Address of the do_something() function: {id(do_something)}")
        print("I'm decorator1")
        func()
        print(f"Address of the 'func' argument: {id(func)}")

    return do_something


@decorator1
def func1():
    print("I'm func1")


print(f"Address of the decorator1() function object: {id(decorator1)}")
print(f"Address of the func1() function object (before decoration): {id(func1)}")

func1()

print(f"Address of the func1() function object (after decoration): {id(func1)}")
print(f"Address of the 'decorator1' variable: {id(decorator1)}")
