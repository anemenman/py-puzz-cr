"""
All integers in the range [-5, 256] are automatically interned:
"""
import sys

print(id(228))
print(id(257))

x = 228
y = 228
print(x is y)

x = 257
y = 257
print(x is y)

x = 228
y = 228
print(id(x))
print(id(y))

x = 388
y = 388
print(id(x))
print(id(y))

# is the same as  id(x)=id(y)
"""
works in python3 interpreter
"""
a = 1234888
b = a
print(a is b)  # prints True

c = 1234888
print(c is a)  # prints False

print(c == a)  # prints True

x = "not normally be interned"
y = "not normally be interned"
print(x is y)  # False

x = sys.intern(x)
y = sys.intern(y)

print(x is y)  # True
