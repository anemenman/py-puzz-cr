"""
Miller-Rabin test for primes, which works for super large n
"""

import random


def even_odd(n):
    s, d = 0, n
    while d % 2 == 0:
        s += 1
        d >>= 1
    return s, d


def Miller_Rabin(a, p):
    s, d = even_odd(p - 1)
    a = pow(a, d, p)
    if a == 1: return True
    for i in range(s):
        if a == p - 1: return True
        a = pow(a, 2, p)
    return False


def is_prime(p):
    if p == 2: return True
    if p <= 1 or p % 2 == 0: return False
    return all(Miller_Rabin(random.randint(2, p - 1), p) for _ in range(40))


assert is_prime(2) is True
assert is_prime(3) is True
assert is_prime(4) is False
assert is_prime(17) is True
assert is_prime(18) is False
assert is_prime(0) is False
assert is_prime(-5) is False
print('Ok')
