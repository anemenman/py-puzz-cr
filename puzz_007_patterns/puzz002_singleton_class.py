class MySingleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if MySingleton.__instance == None:
            MySingleton()

        return MySingleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if MySingleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            MySingleton.__instance = self


my_singleton1 = MySingleton()
# my_singleton2 = MySingleton()# Exception: This class is a singleton!

my_singleton3 = MySingleton.getInstance()
my_singleton5 = MySingleton.getInstance()

print(id(my_singleton1))
print(id(my_singleton3))
print(id(my_singleton5))
