"""
For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).
E. g., with the input [3, 4, 2], your code should return 1 because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more than 369 millions of digits. lastDigit has to
deal with such numbers efficiently.

Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.
"""

"""
Preliminary Analysis
The function we need to write will take two numbers: a base and an exponent, perform the operation
of raising to a power, and output the last digit of the value. Since the value grows rapidly when raised to a power,
calculating the exact value and then finding the last digit is impractical. A more efficient approach is to find
a way to reduce the number of exponents that need to be calculated. Considering only the last
digit, creating a table of all powers of the last digit reveals a pattern:

0: [0],
1: [1],
2: [2, 4, 8, 6],
3: [3, 9, 7, 1],
4: [4, 6],
5: [5],
6: [6],
7: [7, 9, 3, 1],
8: [8, 4, 2, 6],
9: [9, 1]
            
As shown in the table above, all numbers ending in the same digit (0–9) will return to the same digit after
multiplying by themselves four times.
For example, 3 squared is 9, cubed is 27 (the last digit is 7),
to the fourth power is 81 (the last digit is 1), to the fifth power is 243 (the last digit is 3 again),
and multiplying by itself four times gives a full cycle of the last digit. Using this pattern, we can simplify
the calculations.

Let's consider the borderline cases:
1. If the exponent is 0, such as 2^0, the value is 1.
2. If the base is 0, such as 0^2 or 0^0, the value is 0.

Others:
3. Perform division modulo the exponent (mod 4, the remainder is between 0 and 3 plus 4),
then calculate the last digit of the result (mod 10).
A more challenging variation of this problem involves finding the last digit of a series of larger powers.

Notes:
1) To obtain the last digit, we simply need to find the periods of the power from top to bottom.
2) We use n % 4 + 4 because if n % 4 = 0, then we incorrectly obtain x**0.
3) To correctly obtain the period of the remainder after dividing by 4, we need the last two digits of the power, since 
one is not enough.
Example 76 % 4 = 0 и 6 % 4 = 2 in test [7, 6, 21]
"""


def last_digit(lst):
    n = 1
    for x in reversed(lst):
        n = x ** (n if n < 4 else n % 4 + 4)
    return n % 10


assert last_digit([]) == 1
assert last_digit([0, 0]) == 1
assert last_digit([0, 0, 0]) == 0
assert last_digit([1, 2]) == 1
assert last_digit([3, 4, 5]) == 1
assert last_digit([4, 3, 6]) == 4
assert last_digit([7, 6, 21]) == 1
assert last_digit([12, 30, 21]) == 6
assert last_digit([2, 2, 2, 0]) == 4
assert last_digit([937640, 767456, 981242]) == 0
assert last_digit([123232, 694022, 140249]) == 6
assert last_digit([499942, 898102, 846073]) == 6
