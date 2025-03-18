import sys

a = 10
dir(a)
print(sys.getrefcount(a))
b = a
print(sys.getrefcount(a))
print(sys.getrefcount(b))
del a
print(sys.getrefcount(b))

print(sys.getrefcount('new object'))  # 3
print(sys.getrefcount(0))
