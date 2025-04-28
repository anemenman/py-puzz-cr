"""
Создать объект как список, к которому доступ будет начиная с первого элемента, т.е. у него b[1] как a[0] в списке
"""


class NewList(list):
    def __getitem__(self, index):
        if index == 0:
            raise IndexError(f'List index out of range: {index}')
        elif index < 0:
            return super().__getitem__(index)
        return super().__getitem__(index - 1)


list1 = [0, 1, 2]
list2 = NewList(list1)

assert list2[1] == 0
assert list2[2] == 1
assert list2[3] == 2
try:
    print(list2[0])
except IndexError:
    pass

assert list2[-1] == 2  # return by index from end of list(from right)

try:
    print(list2[-100])
except IndexError:
    pass
