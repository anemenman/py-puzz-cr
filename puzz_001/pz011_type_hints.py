def greet(name: str) -> str:
    return "Hello, " + name


class Person:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
