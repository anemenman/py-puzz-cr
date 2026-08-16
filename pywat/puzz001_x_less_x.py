import math


class MyClass:
    def __lt__(self, other):
        return True


x1 = MyClass()
print(x1 < x1)  # True

print(float('NaN') < float('NaN'))  # False
print(math.nan < math.nan)  # False
