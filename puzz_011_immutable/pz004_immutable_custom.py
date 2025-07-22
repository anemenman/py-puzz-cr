"""
Manually Preventing Modification: This involves implementing methods that either return new instances instead
of modifying the existing one or raising errors upon attempted modification.

Benefits of Immutable Classes:
1) Thread Safety:
Immutable objects are inherently thread-safe as their state cannot be changed, eliminating the need for locks
or synchronization in concurrent environments.
2) Predictable Behavior:
Their constant state makes it easier to reason about object behavior and reduces the likelihood of unexpected side
effects.
3) Cacheability:
Immutable objects can be safely cached, improving performance by allowing efficient memoization and caching strategies.
4) Simpler Testing:
Testing is simplified as there's no need to consider different states or mutation scenarios.

"""


class ImmutablePerson:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # No setter methods are provided, making attributes read-only
    # Or, you can explicitly raise an error on attempts to set attributes
    # def __setattr__(self, name, value):
    #     if hasattr(self, name):
    #         raise AttributeError(f"Cannot modify attribute '{name}' of immutable object")
    #     super().__setattr__(name, value)


person = ImmutablePerson("Alice", 30)
print(person)
person.age = 31  # This would be prevented if __setattr__ is implemented
print(person.age)
