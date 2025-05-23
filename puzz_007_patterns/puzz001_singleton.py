"""
PEP 318 – Decorators for Functions and Methods
https://peps.python.org/pep-0318/#examples
"""


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
class MyClassSingleton:
    pass


class MyClass:
    pass


c1 = MyClass()
c2 = MyClass()
print('MyClass-------------')
print(id(c1))
print(id(c2))

cs1 = MyClassSingleton()
cs2 = MyClassSingleton()
print('MyClassSingleton-------------')
print(id(cs1))
print(id(cs2))
