"""
Define a function that takes an integer argument and returns a logical value true or false depending on if the integer
is a prime.
Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other
than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out.
Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.
"""
import math


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


assert is_prime(2) is True
assert is_prime(3) is True
assert is_prime(4) is False
assert is_prime(17) is True
assert is_prime(18) is False
assert is_prime(0) is False
assert is_prime(-5) is False
print('Ok')
