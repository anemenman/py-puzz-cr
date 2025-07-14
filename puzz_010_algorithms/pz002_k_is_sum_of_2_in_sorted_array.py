"""
Задача:

Дан отсортированный массив целых чисел arr длины n.
Дано целое число k.
Нужно найти такие два элемента массива (по их значениям), сумма которых строго равна k.
Если такой пары нет, то найти пару с суммой наиболее близкой к k (по модулю разности) и вывести ее.

Алгоритм (двойной указатель):
Поставим два указателя: left (вначале массива) и right (в конце).
Считаем сумму arr[left] + arr[right].
Если сумма равна k, — наша пара найдена!
Если сумма < k, сдвигаем left вправо (увеличиваем значение суммы).
Если сумма > k, сдвигаем right влево (уменьшаем значение суммы).
Параллельно отслеживаем пару с минимальной разностью |arr[left] + arr[right] - k|, если точного совпадения не найдено.
"""


def find_closest_pair(arr, k):
    left = 0
    right = len(arr) - 1
    closest_pair = (arr[left], arr[right])
    min_diff = abs(arr[left] + arr[right] - k)

    while left < right:
        s = arr[left] + arr[right]
        if s == k:
            return (arr[left], arr[right])  # нашли точную пару
        # Обновляем наиболее близкую пару
        if abs(s - k) < min_diff:
            min_diff = abs(s - k)
            closest_pair = (arr[left], arr[right])
        # Сдвигаем указатели
        if s < k:
            left += 1
        else:
            right -= 1

    return closest_pair  # если точной пары не нашли, возвращаем наиболее близкую


if __name__ == '__main__':
    arr = [1, 3, 4, 7, 10, 14, 18, 23]
    k = 20
    print(find_closest_pair(arr, k))  # (1, 18) или (7, 14) -> 21, ближайшая к 20 сумма

    k = 27
    print(find_closest_pair(arr, k))  # (4, 23) -> 27, ровно

    k = 50
    print(find_closest_pair(arr, k))  # (23, 18) -> 41, максимально близкая к 50
