"""
Найти сумму ряда:
sum = f(n)/(n * (n + 1))
где f(n) - количество единиц в двоичном представлении n
"""
from math import log

n = 100000
print(f'{n} bin: {bin(n)}')
count_1 = bin(n).count('1')
print(f'count of 1: {count_1}')


def count_1(x):
    return bin(x).count('1')


def series_sum(n):
    total = 0
    for k in range(1, n + 1):
        f_k = count_1(k)
        total += f_k / (k * (k + 1))
    return total


sum = series_sum(n)
print(f'sum   = {sum}')

ln_res = log(4)  # ln
print(f'ln(4) = {ln_res}')
