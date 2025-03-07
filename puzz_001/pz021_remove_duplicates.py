"""Дан массив, нужно убрать дублирующиеся элементы, и оставить все которые больше 5"""


def remove_duplicates(numbers):
    result = []
    for index, number in enumerate(numbers):
        if number <= 5:
            continue
        if number in numbers[index + 1:] or number in numbers[:index]:
            continue
        if number not in result:
            result.append(number)

    return result


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
