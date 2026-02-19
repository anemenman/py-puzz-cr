"""
Metaclasses - Simple Django Models

Django is a famous back-end framework written in Python. It has a vast list of features including the creation of
database tables through "models". You can see an example of such model below:

class Person(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
Apart from creating a table it can perform validation, generate HTML forms, and so on. This is possible thanks to
metaclasses. Normally there are better solutions than using metaclasses, but they can be of great help in creating
powerful framework interfaces. This goal of this kata is to learn and understand how such frameworks works.

Your task is to implement a class Model and classes for its fields to support functionality like in the following
example:

class User(Model):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=50)
    email = EmailField()
    is_verified = BooleanField(default=False)
    date_joined = DateTimeField(auto_now=True)
    age = IntegerField(min_value=5, max_value=120, blank=True)


user1 = User(first_name='Liam', last_name='Smith', email='liam@example.com')
user1.validate()

print(user1.date_joined)  # prints date and time when the instance was created
print(user1.is_verified)  # prints False (default value)

user1.age = 256
user1.validate()  # raises ValidationError - age is out of range

user2 = User()
user2.validate()  # raises ValidationError - first three fields are missing and mandatory
The classes which inherit from Model should:

support creation of fields using class-attribute syntax
have a validate method which checks whether all fields are valid
The field types you should implement are described below. Each of them also has parameters blank (default False),
which determines whether None is allowed as a value, and default (default None) which determines the value to be used
if nothing was provided at instantiation time of the Model.

CharField - a string with min_length (default 0) and max_length (default None) parameters, both inclusive if defined
IntegerField - an integer with min_value (default None) and max_value (default None) parameters, both inclusive if
defined
BooleanField - a boolean
DateTimeField - a datetime with an extra parameter auto_now (default False). If auto_now is True and no default value
has been provided, the current datetime should be used automatically at Model instantion time.
EmailField - a string in the format of address@subdomain.domain where address, subdomain, and domain are sequences of
alphabetical characters with min_length (default 0) and max_length (default None) parameters
Each field type should have its own validate method which checks whether the provided value has the correct type and
satisfies the length/value constraints.
"""
import datetime
import re


class ValidationError(Exception):
    pass


class Field:
    def __init__(self, default=None, blank=False):
        self.name = ''
        self._default = default
        self.blank = blank

    @property
    def default(self):
        if callable(self._default):
            return self._default()
        return self._default

    def validate(self, value):
        if not self.blank and value is None:
            raise ValidationError(self.name, 'missing value')

        if value is not None and not self.is_type_ok(value):
            raise ValidationError(self.name, 'wrong type')

    def is_type_ok(self, value):
        return True


class CharField(Field):
    def __init__(self, min_length=0, max_length=None, **kwds):
        super(CharField, self).__init__(**kwds)
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, value):
        super(CharField, self).validate(value)

        if value is not None and self.min_length and len(value) < self.min_length:
            raise ValidationError(self.name, 'too short')

        if value is not None and self.max_length and len(value) > self.max_length:
            raise ValidationError(self.name, 'too long')

    def is_type_ok(self, value):
        return isinstance(value, str)


class EmailField(CharField):
    def validate(self, value):
        super(EmailField, self).validate(value)

        if value is not None and not re.match(r'[.a-z]+@[a-z]+\.[a-z]{2,6}', value):
            raise ValidationError(self.name, 'not valid e-mail')


class BooleanField(Field):
    def is_type_ok(self, value):
        return type(value) == bool


class DateTimeField(Field):
    def __init__(self, auto_now=False, **kwds):
        if auto_now and kwds.get('default') is None:
            kwds['default'] = datetime.datetime.now
        super(DateTimeField, self).__init__(**kwds)
        self.auto_now = auto_now

    def is_type_ok(self, value):
        return isinstance(value, datetime.datetime)


class IntegerField(Field):
    def __init__(self, min_value=None, max_value=None, **kwds):
        super(IntegerField, self).__init__(**kwds)
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        super(IntegerField, self).validate(value)

        if value is not None and self.min_value and value < self.min_value:
            raise ValidationError(self.name, 'too small')

        if value is not None and self.max_value and value > self.max_value:
            raise ValidationError(self.name, 'too big')

    def is_type_ok(self, value):
        return type(value) == int


class ModelMeta(type):
    def __new__(meta, class_name, bases, class_dict):
        new_class_dict = {}

        for attribute_name, attribute in class_dict.items():
            if not isinstance(attribute, Field):
                new_class_dict[attribute_name] = attribute
                continue
            attribute.name = attribute_name
            new_class_dict.setdefault('_attributes_', {}).setdefault(attribute_name, attribute)

        return super(ModelMeta, meta).__new__(meta, class_name, bases, new_class_dict)


class Model(metaclass=ModelMeta):
    _attributes_ = {}

    def __init__(self, **kwds):
        for attr in self._attributes_.values():
            setattr(self, attr.name, kwds.get(attr.name, attr.default))

    def validate(self):
        for attr in self._attributes_.values():
            attr.validate(getattr(self, attr.name))


class User(Model):
    first_name = CharField(max_length=30, default='Adam')
    last_name = CharField(max_length=50)
    email = EmailField()
    is_verified = BooleanField(default=False)
    date_joined = DateTimeField(auto_now=True)
    age = IntegerField(min_value=5, max_value=120, blank=True)


user1 = User(first_name='Liam', last_name='Smith', email='liam@example.com')
user1.validate()

print(user1.date_joined)
print(user1.is_verified)

try:
    user1.age = 256
    user1.validate()
except ValidationError as e:
    print(e)

user2 = User()
try:
    user2.validate()
except ValidationError as e:
    print(e)
