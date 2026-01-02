"""
The Millionth Fibonacci Kata

In this kata you will have to calculate fib(n) where:

fib(0) := 0
fib(1) := 1
fib(n + 2) := fib(n + 1) + fib(n)
Write an algorithm that can handle n up to 2000000.

Your algorithm must output the exact integer answer, to full precision. Also, it must correctly handle negative numbers
as input.

HINT I: Can you rearrange the equation fib(n + 2) = fib(n + 1) + fib(n) to find fib(n) if you already know fib(n + 1)
and fib(n + 2)? Use this to reason what value fib has to have for negative values.

HINT II: See https://web.archive.org/web/20220614001843/https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.4
"""
import time


def pow_matrix(x, n, i_matrix, mult):
    """
    Returns x raised to the nth power. Assumes that I is the identity matrix, which is multiplied by mult,
    and n is a positive integer.
    """
    if n == 0:
        return i_matrix
    elif n == 1:
        return x
    else:
        y = pow_matrix(x, n // 2, i_matrix, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y


def identity_matrix(n):
    """Returns the n by n identity matrix"""
    r = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]


def matrix_multiply(a, b):
    bt = list(zip(*b))
    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in bt] for row_a in a]


"""Complexity is O(log(n))"""


def fib(n):
    abs_n = n
    if n < 0:
        abs_n = -n
    f = pow_matrix([[1, 1], [1, 0]], abs_n, identity_matrix(2), matrix_multiply)
    result = f[0][1]

    if n < 0 and (abs_n + 1) % 2 != 0:
        result = -result

    return result


start = time.time()

assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5

assert fib(-1) == 1
assert fib(-6) == -8
assert fib(-96) == -51680708854858323072
assert fib(-96) == -51680708854858323072
assert fib(
    -500) == -139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
assert fib(
    1000) == 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875

print(time.time() - start)
