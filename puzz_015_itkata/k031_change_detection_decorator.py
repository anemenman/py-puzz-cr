"""
Your task is to write a class decorator named change_detection that traces the changes of the attributes of the defined
class. When referred on an object, each attribute - defined either on object level or class level - should interpret an
additional property called get_change which returns one of the following strings:

''      -  if the attribute isn't defined
'INIT'  -  if the attribute was just created
'MOD'   -  if the value of the attribute was changed from its initial value at least once
'DEL'   -  if the attribute gets deleted on the object
We can assume that each attribute has its copy constructor implemented.

Example
As an example, after the following class definition, the python terminal output should show as follows.

@change_detection
class Struct:
    x = 42
    def __init__(self, y=0):
        self.y = y

a = Struct(11)

Struct.x == 42
# Struct.x.get_change - will not be tested

a.x, a.y == 42, 11
a.x.get_change == a.y.get_change == 'INIT'

a.z.get_change == ''

a.y = 11
a.y.get_change == 'INIT'

a.y = 12
a.y.get_change == 'MOD'

a.x = '42'
a.x.get_change == 'MOD'

del a.y
a.y.get_change == 'DEL'
Note that the behaviour in case of any other operation on an undefined attribute is up to you: AttributeError might be
raised or just a None, NONE or NO_SUCH might be returned.

For your convenience, two objects: NO_SUCH and NONE are predefined, which has copy constructor. Also, the envelope
class Bool of the nonsubclassable bool is predefined in case you might need it...

Good luck!
"""


def change_detection(cls):
    class AttrWrapper:
        def __init__(self, value, get_change='INIT'):
            self.value = value
            self.get_change = get_change

        def __getattr__(self, name):
            return getattr(self.value, name)

        def __repr__(self):
            return str(self.value)

        def __bool__(self):
            return bool(self.value)

        def __call__(self):
            return self.value()

        def __eq__(self, other):
            return self.value == other

        def __add__(self, other):
            return self.value + other

        def __sub__(self, other):
            return self.value - other

        def __mul__(self, other):
            return self.value * other

        def __truediv__(self, other):
            return self.value / other

        def __radd__(self, other):
            return other + self.value

        def __rsub__(self, other):
            return other - self.value

        def __rmul__(self, other):
            return other * self.value

        def __rtruediv__(self, other):
            return other / self.value

    def __getattribute__(self, name):
        try:
            attr = super(cls, self).__getattribute__(name)
            if type(attr) is not AttrWrapper:
                new_attr = AttrWrapper(attr)
                super(cls, self).__setattr__(name, new_attr)
                return new_attr
            return attr
        except:
            return AttrWrapper(None, '')

    def __setattr__(self, name, value):
        target = getattr(self, name, None)
        if type(target) is not AttrWrapper or not target.get_change:
            super(cls, self).__setattr__(name, AttrWrapper(value))
        elif target.value != value or type(target.value) is not type(value):
            target.value = value
            target.get_change = 'MOD'

    def __delattr__(self, name):
        target = getattr(self, name)
        target.value = None
        target.get_change = 'DEL'

    setattr(cls, '__setattr__', __setattr__)
    setattr(cls, '__getattribute__', __getattribute__)
    setattr(cls, '__delattr__', __delattr__)

    return cls


class U:
    def __init__(self, x=0):
        self.x = x.x if isinstance(self, x.__class__) else x

    def f(self, y):
        return self.x + y


@change_detection
class Struct:
    x = 42
    no = None

    def __init__(self, y=0):
        self.y = y
        self.u = U(4)
        self.uuu = None

    def f(self):
        if self.tt.get_change:
            self.tt += 1
        else:
            self.tt = 0


a = Struct(11)
