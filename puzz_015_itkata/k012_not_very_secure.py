"""
In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None,
so you don't have to check that.
The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore
"""
import re


def alphanumeric(password: str) -> bool:
    if not password:
        return False

    for char in password:
        if not (char.isalnum() and char.isascii()):
            return False

    if ' ' in password or '_' in password:
        return False

    return True


def alphanumeric_v2(string):
    return string.isalnum()


def alphanumeric_v3(string):
    return bool(re.search(r'^[0-9a-zA-Z]+$', string))


assert alphanumeric('Hello123') is True
assert alphanumeric('Hello 123') is False
assert alphanumeric('Hello_123') is False
assert alphanumeric('123') is True
assert alphanumeric('') is False
assert alphanumeric('!@#$$%') is False

assert alphanumeric_v2('Hello123') is True
assert alphanumeric_v2('Hello 123') is False
assert alphanumeric_v2('Hello_123') is False
assert alphanumeric_v2('123') is True
assert alphanumeric_v2('') is False
assert alphanumeric_v2('!@#$$%') is False

assert alphanumeric_v3('Hello123') is True
assert alphanumeric_v3('Hello 123') is False
assert alphanumeric_v3('Hello_123') is False
assert alphanumeric_v3('123') is True
assert alphanumeric_v3('') is False
assert alphanumeric_v3('!@#$$%') is False
