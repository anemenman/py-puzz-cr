"""
Debugger

Imagine you have a large project where is suddenly going something very messy. You are not able to guess what it is and
don't want to debug all the code through. Your project has one base class.

In this kata you will write metaclass Meta for your base class, which will collect data about all attribute accesses
and method calls in all project classes. From this data you can then better guess what is happening or which method
call is bottleneck of your app.

We will use class Debugger to store the data. Method call collection should look like this:

Debugger.method_calls.append({
    'class': ..., # class object, not string
    'method': ..., # method name, string
    'args': args, # all args, including self
    'kwargs': kwargs
})
Attribute access collection should look like this:

Debugger.attribute_accesses.append({
    'action': 'set', # set/get
    'class': ..., # class object, not string
    'attribute': ..., # name of attribute, string
    'value': value # actual value
})
You should NOT log calls of getter/setter methods that you might create by meta class.
"""


class Debugger:
    method_calls = []
    attribute_accesses = []


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        # Wrap all methods except special/magic and those injected by meta itself
        for attr, obj in list(namespace.items()):
            # Only wrap if it's a function (not @property etc) and not static/class method or dunder
            if callable(obj) and not attr.startswith("__") and not isinstance(obj, (staticmethod, classmethod)):
                def make_wrapper(method_name, method):
                    def wrapper(self, *args, **kwargs):
                        Debugger.method_calls.append({
                            'class': self.__class__,
                            'method': method_name,
                            'args': (self,) + args,
                            'kwargs': kwargs,
                        })
                        return method(self, *args, **kwargs)

                    return wrapper

                namespace[attr] = make_wrapper(attr, obj)

        # Inject custom __getattribute__ and __setattr__
        orig_getattribute = namespace.get('__getattribute__', None)
        orig_setattr = namespace.get('__setattr__', None)

        def __getattribute__(self, name):
            # Don't log meta's injected dunder methods or Debugger access
            if name not in ('__class__', '__dict__', '__weakref__'):
                value = object.__getattribute__(self, name)
                if not callable(value):
                    Debugger.attribute_accesses.append({
                        'action': 'get',
                        'class': self.__class__,
                        'attribute': name,
                        'value': value,
                    })
                return value
            else:
                return object.__getattribute__(self, name)

        def __setattr__(self, name, value):
            Debugger.attribute_accesses.append({
                'action': 'set',
                'class': self.__class__,
                'attribute': name,
                'value': value,
            })
            object.__setattr__(self, name, value)

        # Prevent wrapping the base Exception/Debugger, etc.
        if '__getattribute__' not in namespace:
            namespace['__getattribute__'] = __getattribute__
        if '__setattr__' not in namespace:
            namespace['__setattr__'] = __setattr__

        return super().__new__(mcs, name, bases, namespace)


class Foo(object, metaclass=Meta):
    def __init__(self, x):
        self.x = x

    def bar(self, v):
        return (self.x, v)


a = Foo(1)
a.bar(2)

calls = Debugger.method_calls
acc = Debugger.attribute_accesses

print(calls)
# print(acc)
print(len(calls))
assert len(calls) == 2

print("Test collected method calls")

print("Call to init should be collected")
assert calls[0]['args'] == (a, 1)

print("Call to bar should be collected")
assert calls[1]['args'] == (a, 2)

print("Test collected attribute accesses")
accesses = Debugger.attribute_accesses

assert len(accesses) == 3

print("Attribute set in init should be collected")
assert accesses[0]['action'] == 'set'
assert accesses[0]['attribute'] == 'x'
assert accesses[0]['value'] == 1

print("Method get should be collected too")
assert accesses[1]['action'] == 'get'
assert accesses[1]['attribute'] == 'bar'

print("Attribute get should be collected")
assert accesses[2]['action'] == 'get'
assert accesses[2]['attribute'] == 'x'
