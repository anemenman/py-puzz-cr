"""
In Python, a mixin is a class designed to provide specific, reusable functionality to other classes through multiple
inheritance. It is not intended to be instantiated on its own but rather "mixed in" to extend the capabilities of
existing classes without forming a strict "is-a" hierarchical relationship.
"""


# Mixin class
class LoggerMixin:
    def log(self, message):
        print(f"LOG: {message}")


# Use mixin
class MyClass(LoggerMixin):
    def do_something(self):
        self.log("Start do something...")
        self.log("Finished do something...")


my_obj = MyClass()
my_obj.do_something()
