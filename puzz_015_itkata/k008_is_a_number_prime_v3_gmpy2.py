import gmpy2


def is_prime(num):
    return gmpy2.is_prime(num) if num > 0 else False


assert is_prime(2) is True
assert is_prime(3) is True
assert is_prime(4) is False
assert is_prime(17) is True
assert is_prime(18) is False
assert is_prime(0) is False
assert is_prime(-5) is False
print('Ok')
