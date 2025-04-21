data1 = {'e', 'f', 'g'}
print(type(data1))
print(data1)
data1.add('h')
print(data1)

data2 = frozenset(data1)
print(type(data2))
print(data2)
data2.add('i')  # AttributeError: 'frozenset' object has no attribute 'add'
print(data2)
