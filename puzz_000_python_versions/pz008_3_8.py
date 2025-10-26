"""Python 3.8 was released on October 14th, 2019."""
from datetime import date

"""New Features"""

"""Assignment expressions
There is new syntax := that assigns values to variables as part of a larger expression. It is affectionately known as “the walrus operator”

In this example, the assignment expression helps avoid calling len() twice:
"""
a = 'test1234567'
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")

"""Positional-only parameters"""
"""In the following example, parameters a and b are positional-only, while c or d can be positional or keyword, and e or f are required to be keywords:"""


def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


f(10, 20, 30, d=40, e=50, f=60)
# f(10, b=20, c=30, d=40, e=50, f=60)  # b cannot be a keyword argument
# f(10, 20, 30, 40, 50, f=60)  # e must be a keyword argument


"""f-strings support = for self-documenting expressions and debugging"""
user = 'eric_idle'
member_since = date(1975, 7, 31)
print(f'{user=} {member_since=}')
