"""
Double Checked Locking Singleton Design pattern
It is easy to notice that once an object is created, the synchronization of the threading is no longer useful because now the object will never be equal to None and any sequence of operations will lead to consistent results.
So, when the object will be equal to None, then only we will acquire the Lock on the getInstance method.
"""
import threading


class SingletonDoubleChecked(object):
    # resources shared by each and every
    # instance

    __singleton_lock = threading.Lock()
    __singleton_instance = None

    # define the classmethod
    @classmethod
    def instance(cls):

        # check for the singleton instance
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()

        # return the singleton instance
        return cls.__singleton_instance


class A(SingletonDoubleChecked):
    pass


s1 = SingletonDoubleChecked.instance()
s2 = SingletonDoubleChecked.instance()

print(id(s1))
print(id(s2))

a1 = A()
a2 = A()

print(id(a1))
print(id(a2))

aa1 = A.instance()
aa2 = A.instance()

print(id(aa1))
print(id(aa2))
