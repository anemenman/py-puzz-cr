"""
Monostate/Borg Singleton Design pattern

Singleton behavior can be implemented by Borg's pattern but instead of having only one instance of the class,
there are multiple instances that share the same state.
"""


class BorgSingleton:
    __shared_state = dict()

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'aaa'

    def __str__(self):
        return self.state


bs1 = BorgSingleton()
bs2 = BorgSingleton()
bs3 = BorgSingleton()

bs1.state = 'bbb'
bs2.state = 'ccc'

print("-------------test 1:")
print(bs1)
print(bs2)
print(bs3)

bs3.state = 'ddd'

print("-------------test 2:")
print(bs1)
print(bs2)
print(bs3)
