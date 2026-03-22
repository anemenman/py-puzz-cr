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
    """
    Декоратор класса для отслеживания изменений атрибутов.
    Добавляет каждому атрибуту метод get_change, возвращающий статус изменения.
    """

    class AttributeWithChange:
        """Класс-обертка для атрибута с отслеживанием изменений"""

        def __init__(self, value, status='INIT'):
            self.value = value
            self._status = status
            self._initial_value = value

        @property
        def get_change(self):
            return self._status

        def set_value(self, new_value):
            """Обновляет значение и статус при изменении"""
            if self._status == 'DEL':
                self._status = 'INIT'
                self._initial_value = new_value
            elif new_value != self._initial_value:
                self._status = 'MOD'
            self.value = new_value

        def delete(self):
            """Помечает атрибут как удаленный"""
            self._status = 'DEL'
            self.value = None

        def __eq__(self, other):
            return self.value == other

        def __str__(self):
            return str(self.value)

        def __repr__(self):
            return repr(self.value)

    class WrappedClass(cls):
        """Обернутый класс с отслеживанием изменений"""

        def __init__(self, *args, **kwargs):
            # Инициализируем хранилище атрибутов
            self._change_tracker = {}

            # Вызываем оригинальный __init__
            super().__init__(*args, **kwargs)

            # Отслеживаем все существующие атрибуты экземпляра
            for attr_name in dir(self):
                if not attr_name.startswith('_') and attr_name != 'get_change':
                    try:
                        value = getattr(self, attr_name)
                        if not isinstance(value, AttributeWithChange):
                            self._change_tracker[attr_name] = AttributeWithChange(value)
                            setattr(self, attr_name, self._change_tracker[attr_name])
                    except AttributeError:
                        pass

            # Отслеживаем атрибуты класса
            for attr_name in dir(cls):
                if not attr_name.startswith('_') and attr_name != 'get_change':
                    try:
                        value = getattr(cls, attr_name)
                        if not isinstance(value, AttributeWithChange) and not callable(value):
                            if attr_name not in self._change_tracker:
                                self._change_tracker[attr_name] = AttributeWithChange(value)
                                setattr(self, attr_name, self._change_tracker[attr_name])
                    except AttributeError:
                        pass

        def __setattr__(self, name, value):
            """Перехватываем установку атрибутов"""
            if name == '_change_tracker' or name.startswith('__'):
                super().__setattr__(name, value)
                return

            if hasattr(self, '_change_tracker'):
                if name in self._change_tracker:
                    # Обновляем существующий атрибут
                    self._change_tracker[name].set_value(value)
                else:
                    # Создаем новый атрибут
                    self._change_tracker[name] = AttributeWithChange(value, 'INIT')

                # Устанавливаем значение через обертку
                super().__setattr__(name, self._change_tracker[name])
            else:
                super().__setattr__(name, value)

        def __getattr__(self, name):
            """Перехватываем доступ к несуществующим атрибутам"""
            if name.startswith('_'):
                raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

            if hasattr(self, '_change_tracker'):
                if name not in self._change_tracker:
                    # Возвращаем специальный объект для несуществующих атрибутов
                    return type('MissingAttribute', (), {
                        'get_change': '',
                        'value': None
                    })()

            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

        def __delattr__(self, name):
            """Перехватываем удаление атрибутов"""
            if hasattr(self, '_change_tracker') and name in self._change_tracker:
                self._change_tracker[name].delete()
                # Не удаляем атрибут полностью, а только помечаем как удаленный
            else:
                super().__delattr__(name)

    return WrappedClass


print("Ok")


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

print(a)
print(a.y)
