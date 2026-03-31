"""
When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the
process --myjinxin2015 said

Task
We have a rectangular cake with some raisins on it:

cake =
  ........
  ..o.....
  ...o....
  ........
// o is the raisins
We need to cut the cake evenly into n small rectangular pieces, so that each small cake has 1 raisin. n is not an
argument, it is the number of raisins contained inside the cake:

cake =
  ........
  ..o.....
  ...o....
  ........

result should be an array:
  [
     ........
     ..o.....
  ,
     ...o....
     ........
  ]
// In order to clearly show, we omit the quotes and "\n"
If there is no solution, return an empty array []

Note
The number of raisins is always more than 1 and less than 10.
If there are multiple solutions, select the one with the largest width of the first element of the array.
(See also the examples below.)
Evenly cut into n pieces, meaning the same area. But their shapes can be different. (See also the examples below.)
In the result array, the order of pieces is from top to bottom and from left to right (according to the location of
the upper left corner).
Each piece of cake should be rectangular.
Examples
An example of multiple solutions:
cake =
  .o......
  ......o.
  ....o...
  ..o.....

In this test case, we can found three solution:
solution 1 (horizontal cutting):
  [
    .o......  //piece 1
  ,
    ......o.  //piece 2
  ,
    ....o...  //piece 3
  ,
    ..o.....  //piece 4
  ]

solution 2 (vertical cutting):
  [
    .o  //piece 1
    ..
    ..
    ..
  ,
    ..  //piece 2
    ..
    ..
    o.
  ,
    ..  //piece 3
    ..
    o.
    ..
  ,
    ..  //piece 4
    o.
    ..
    ..
  ]

solution 3 (cross cutting):
  [
    .o..  //piece 1
    ....
  ,
    ....  //piece 2
    ..o.
  ,
    ....  //piece 3
    ..o.
  ,
    o...  //piece 4
    ....
  ]

we need choose solution 1 as result
An example of different shapes:
cake =
  .o.o....
  ........
  ....o...
  ........
  .....o..
  ........

the result should be:
  [
    .o      //pieces 1
    ..
    ..
    ..
    ..
    ..
  ,
    .o....  //pieces 2
    ......
  ,
    ..o...  //pieces 3
    ......
  ,
    ...o..  //pieces 4
    ......
  ]
Although they have different shapes,
they have the same area(2 x 6 = 12 and 6 x 2 = 12).
An example of no solution case:
cake =
  .o.o....
  .o.o....
  ........
  ........
  ........
  ........
the result should be []
"""


def cut(cake):
    if not cake or not cake[0]:
        return []

    rows = len(cake)
    cols = len(cake[0])
    total_area = rows * cols

    # Найти позиции всех изюминок
    raisins = []
    for r in range(rows):
        for c in range(cols):
            if cake[r][c] == 'o':
                raisins.append((r, c))

    n = len(raisins)
    # Проверка базовых условий
    if n <= 1 or total_area % n != 0:
        return []

    target_area = total_area // n
    if target_area <= 0:
        return []

    def get_rect_cells(r1, c1, r2, c2):
        """Вернуть список всех ячеек в прямоугольнике [r1,r2] x [c1,c2] включительно"""
        return [(r, c) for r in range(r1, r2 + 1) for c in range(c1, c2 + 1)]

    def count_raisins_in_rect(r1, c1, r2, c2):
        """Посчитать количество изюминок в прямоугольнике"""
        return sum(1 for rr, cc in raisins if r1 <= rr <= r2 and c1 <= cc <= c2)

    # Предварительно вычислить все валидные прямоугольники для каждой изюминки
    raisin_rects = {i: [] for i in range(n)}

    for i, (rr, cc) in enumerate(raisins):
        # Перебрать все возможные размеры прямоугольников с нужной площадью
        for h in range(1, rows + 1):
            if target_area % h != 0:
                continue
            w = target_area // h
            if w < 1 or w > cols:
                continue

            # Перебрать все позиции для прямоугольника размера h×w
            for r1 in range(rows - h + 1):
                r2 = r1 + h - 1
                for c1 in range(cols - w + 1):
                    c2 = c1 + w - 1

                    # Прямоугольник должен содержать текущую изюминку
                    if not (r1 <= rr <= r2 and c1 <= cc <= c2):
                        continue
                    # Прямоугольник должен содержать ровно одну изюминку (эту)
                    if count_raisins_in_rect(r1, c1, r2, c2) != 1:
                        continue

                    # Сохранить прямоугольник: координаты и ширину
                    raisin_rects[i].append((r1, c1, r2, c2, w))

        # Если для какой-то изюминки нет валидных прямоугольников — решения нет
        if not raisin_rects[i]:
            return []

    solutions = []

    def backtrack(assigned, covered, current):
        """
        assigned: множество индексов изюминок, которым уже назначен прямоугольник
        covered: множество ячеек, покрытых назначенными прямоугольниками
        current: список пар (индекс_изюминки, прямоугольник) для текущего решения
        """
        # Все изюминки назначены
        if len(assigned) == n:
            # Проверить, покрыт ли весь торт
            if len(covered) == total_area:
                solutions.append(list(current))
            return

        # Выбрать следующую неназначенную изюминку
        raisin_idx = next(i for i in range(n) if i not in assigned)

        # Попробовать каждый валидный прямоугольник для этой изюминки
        for rect in raisin_rects[raisin_idx]:
            r1, c1, r2, c2, w = rect
            cells = set(get_rect_cells(r1, c1, r2, c2))

            # Пропустить, если прямоугольник пересекается с уже покрытыми ячейками
            if cells & covered:
                continue

            # Назначить прямоугольник
            assigned.add(raisin_idx)
            covered |= cells
            current.append((raisin_idx, rect))

            # Рекурсивный вызов
            backtrack(assigned, covered, current)

            # Откат (backtrack)
            current.pop()
            for cell in cells:
                covered.discard(cell)
            assigned.remove(raisin_idx)

    # Запустить поиск с возвратом
    backtrack(set(), set(), [])

    if not solutions:
        return []

    def solution_to_pieces(sol):
        """
        Преобразовать решение в формат вывода:
        - Отсортировать куски по позиции левого верхнего угла
        - Вернуть список кусков и ширину первого куска
        """
        pieces_with_pos = []
        for raisin_idx, (r1, c1, r2, c2, w) in sol:
            # Извлечь подстроки для этого куска торта
            piece = [cake[r][c1:c2 + 1] for r in range(r1, r2 + 1)]
            pieces_with_pos.append((r1, c1, w, piece))

        # Сортировка: сверху вниз, слева направо по левому верхнему углу
        pieces_with_pos.sort(key=lambda x: (x[0], x[1]))
        pieces = [p[3] for p in pieces_with_pos]
        first_width = pieces_with_pos[0][2]
        return pieces, first_width

    # Найти лучшее решение: максимальная ширина первого куска
    best_pieces = None
    best_width = -1

    for sol in solutions:
        pieces, first_w = solution_to_pieces(sol)
        if first_w > best_width:
            best_width = first_w
            best_pieces = pieces

    return best_pieces if best_pieces else []
