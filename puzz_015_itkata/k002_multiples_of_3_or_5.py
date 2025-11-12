"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
Note: If a number is a multiple of both 3 and 5, only count it once.
Courtesy of projecteuler.net (Problem 1)
"""


def sum_multiples_of_3_and_5(number):
    if number < 0:
        return 0

    sum_of_multiples = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i

    return sum_of_multiples


def sum_multiples_of_3_and_5_v2(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


print(sum_multiples_of_3_and_5(10))
print(sum_multiples_of_3_and_5(200))
print(sum_multiples_of_3_and_5(-1))
