"""Дан массив, нужно убрать дублирующиеся элементы, и оставить все которые больше 5"""


def remove_duplicates(numbers):
    return [
        num for index, num in enumerate(numbers)
        if num > 5 and num not in numbers[index + 1:] and num not in numbers[:index]
    ]


def test_remove_duplicates():
    result = remove_duplicates([1, 5, 8, 8, 10])
    assert result == [10], f'Fail: {result}'

    result = remove_duplicates([])
    assert result == [], f'Fail: {result}'

    result = remove_duplicates([1, 2, 3, 4])
    assert result == [], f'Fail: {result}'

    print('Все тесты пройдены')


if __name__ == '__main__':
    test_remove_duplicates()
