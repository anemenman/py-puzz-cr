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


class ValidationError(Exception):
    pass


class Field:
    def __init__(self, *, blank=False, default=None):
        self.blank = blank
        self.default = default
        self.name = None  # Устанавливается во время создания класса

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance._values.get(self.name, self.default)

    def __set__(self, instance, value):
        instance._values[self.name] = value

    def contribute_to_class(self, cls, name):
        self.name = name

    def validate(self, value):
        if value is None:
            if not self.blank:
                raise ValidationError(f"{self.name} cannot be blank")
            return
        self._validate_type_and_constraints(value)

    def _validate_type_and_constraints(self, value):
        pass


class CharField(Field):
    def __init__(self, *, min_length=0, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.min_length = min_length
        self.max_length = max_length

    def _validate_type_and_constraints(self, value):
        if not isinstance(value, str):
            raise ValidationError(f"{self.name} must be a string")
        if len(value) < self.min_length:
            raise ValidationError(f"{self.name} is too short")
        if self.max_length is not None and len(value) > self.max_length:
            raise ValidationError(f"{self.name} is too long")


class IntegerField(Field):
    def __init__(self, *, min_value=None, max_value=None, **kwargs):
        super().__init__(**kwargs)
        self.min_value = min_value
        self.max_value = max_value

    def _validate_type_and_constraints(self, value):
        if not isinstance(value, int):
            raise ValidationError(f"{self.name} must be an integer")
        if self.min_value is not None and value < self.min_value:
            raise ValidationError(f"{self.name} cannot be less than {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValidationError(f"{self.name} cannot be greater than {self.max_value}")


class BooleanField(Field):
    def _validate_type_and_constraints(self, value):
        if not isinstance(value, bool):
            raise ValidationError(f"{self.name} must be a boolean")


class DateTimeField(Field):
    def __init__(self, *, auto_now=False, **kwargs):
        super().__init__(**kwargs)
        self.auto_now = auto_now

    def _validate_type_and_constraints(self, value):
        if not isinstance(value, datetime):
            raise ValidationError(f"{self.name} must be a datetime")


class EmailField(CharField):
    EMAIL_RE = re.compile(r'^[A-Za-z]+@[A-Za-z]+\.[A-Za-z]+$')

    def _validate_type_and_constraints(self, value):
        super()._validate_type_and_constraints(value)
        if not EmailField.EMAIL_RE.match(value):
            raise ValidationError(f"{self.name} is not a valid email")


class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        fields = {}
        # Собираем поля из базовых классов, затем из этого класса
        for base in reversed(bases):
            if hasattr(base, '_fields'):
                fields.update(base._fields)
        for k, v in list(attrs.items()):
            if isinstance(v, Field):
                v.contribute_to_class(cls, k)
                fields[k] = v
        attrs['_fields'] = fields
        return super().__new__(cls, name, bases, attrs)


class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        self._values = {}
        for name, field in self._fields.items():
            if name in kwargs:
                value = kwargs[name]
            elif isinstance(field, DateTimeField) and field.auto_now and field.default is None:
                value = datetime.now()
            elif field.default is not None:
                value = field.default() if callable(field.default) else field.default
            else:
                value = None
            setattr(self, name, value)

    def validate(self):
        for name, field in self._fields.items():
            value = getattr(self, name)
            field.validate(value)


class User(Model):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=50)
    email = EmailField()
    is_verified = BooleanField(default=False)
    date_joined = DateTimeField(auto_now=True)
    age = IntegerField(min_value=5, max_value=120, blank=True)


# Пример создания нового пользователя
user1 = User(first_name='Liam', last_name='Smith', email='liam@example.com')
user1.validate()

print(user1.date_joined)  # выводит дату и время создания
print(user1.is_verified)  # выводит False (значение по умолчанию)

try:
    user1.age = 256
    user1.validate()  # вызывает ValidationError - age is out of range
except ValidationError as e:
    print(e)  # выводит ошибку валидации

user2 = User()
try:
    user2.validate()  # вызывает ValidationError - поля обязательны
except ValidationError as e:
    print(e)  # выводит ошибку валидации
