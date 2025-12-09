"""
The purpose of this kata is to write a program that can do some algebra.

Write a function expand that takes in an expression with a single, one character variable, and expands it.
The expression is in the form (ax+b)^n where a and b are integers which may be positive or negative, x is any single
character variable, and n is a natural number. If a = 1, no coefficient will be placed in front of the variable.
If a = -1, a "-" will be placed in front of the variable.

The expanded form should be returned as a string in the form ax^b+cx^d+ex^f... where a, c, and e are the coefficients
of the term, x is the original one character variable that was passed in the original expression and b, d, and f, are
the powers that x is being raised to in each term and are in decreasing order.

If the coefficient of a term is zero, the term should not be included. If the coefficient of a term is one, the
coefficient should not be included. If the coefficient of a term is -1, only the "-" should be included. If the power
of the term is 0, only the coefficient should be included. If the power of the term is 1, the caret and power should
be excluded.

Examples:
expand("(x+1)^2")      # returns "x^2+2x+1"
expand("(p-1)^3")      # returns "p^3-3p^2+3p-1"
expand("(2f+4)^6")     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
expand("(-2a-4)^0")    # returns "1"
expand("(-12t+43)^2")  # returns "144t^2-1032t+1849"
expand("(r+0)^203")    # returns "r^203"
expand("(-x-1)^2")     # returns "x^2+2x+1"
"""
import re
from math import comb


def expand(expression):
    expression = expression.replace(" ", "")
    start = expression.index('(')
    end = expression.index(')')
    inner_expr = expression[start + 1:end]
    n = int(expression[end + 1:].replace("^", ""))

    if n == 0:
        return "1"

    match = re.match(r'([+-]?\d*)([a-zA-Z]+)([+-]?\d*)', inner_expr)

    if match:
        a = match.group(1)
        var_name = match.group(2)
        b = match.group(3)
    else:
        raise ValueError("Invalid expression format")

    if not a:
        a = 1
    if a == "-":
        a = -1
    if not b:
        b = 0

    a = int(a)
    b = int(b)

    terms = []
    for k in range(n + 1):
        coeff = comb(n, k) * (a ** (n - k)) * (b ** k)

        if coeff != 0:
            variable_exponent = n - k
            if variable_exponent > 1:
                if coeff == 1:
                    coeff = ""
                if coeff == -1:
                    coeff = "-"
                term = f"{coeff}{var_name}^{variable_exponent}"
            elif variable_exponent == 1:
                if coeff == 1:
                    coeff = ""
                if coeff == -1:
                    coeff = "-"
                term = f"{coeff}{var_name}"
            else:
                term = str(coeff)

            terms.append(term)

    result = '+'.join(terms).replace('+-', '-')

    return result


assert expand("(x+1)^0") == "1"
assert expand("(x+1)^1") == "x+1"
assert expand("(x+1)^2") == "x^2+2x+1"
assert expand("(x-1)^0") == "1"
assert expand("(x-1)^1") == "x-1"
assert expand("(x-1)^2") == "x^2-2x+1"
assert expand("(5m+3)^4") == "625m^4+1500m^3+1350m^2+540m+81"
assert expand("(2x-3)^3") == "8x^3-36x^2+54x-27"
assert expand("(7x-7)^0") == "1"
assert expand("(-5m+3)^4") == "625m^4-1500m^3+1350m^2-540m+81"
assert expand("(-2k-3)^3") == "-8k^3-36k^2-54k-27"
assert expand("(-7x-7)^0") == "1"
assert expand("(-b-7)^4") == "b^4+28b^3+294b^2+1372b+2401"
assert expand("(-6d+13)^1") == "-6d+13"
assert expand("(-o-12)^1") == "-o-12"
