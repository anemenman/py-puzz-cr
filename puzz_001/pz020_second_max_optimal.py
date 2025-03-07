def two_max(array):
    if len(array) < 2:
        return None

    if array[0] > array[1]:
        max_1, max_2 = array[0], array[1]
    else:
        max_1, max_2 = array[1], array[0]

    index = 2

    while max_1 == max_2 and index < len(array):
        if max_1 > array[index]:
            max_2 = array[index]
        elif max_1 < array[index]:
            max_1 = array[index]
        index += 1

    if max_1 == max_2:
        return None

    for num in array[index:]:
        if num > max_1:
            max_2 = max_1
            max_1 = num
        elif num > max_2:
            max_2 = num

    return max_2


def test_two_max():
    result = two_max([3, 2, -10, 2, 100, 45])
    assert result == 45, f'Wrong answer: {result}'

    result = two_max([100, 100, 99])
    assert result == 99, f'Wrong answer: {result}'

    result = two_max([1])
    assert result is None, f'Wrong answer: {result}'

    result = two_max([])
    assert result is None, f'Wrong answer: {result}'

    print('Все тесты пройдены')


if __name__ == '__main__':
    test_two_max()
