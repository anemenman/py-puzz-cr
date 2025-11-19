"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five()))    #  must return 35
four(plus(nine()))      #  must return 13
eight(minus(three()))   #  must return 5
six(divided_by(two()))  #  must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""


def zero(func=None):
    return calculate(0, func)


def one(func=None):
    return calculate(1, func)


def two(func=None):
    return calculate(2, func)


def three(func=None):
    return calculate(3, func)


def four(func=None):
    return calculate(4, func)


def five(func=None):
    return calculate(5, func)


def six(func=None):
    return calculate(6, func)


def seven(func=None):
    return calculate(7, func)


def eight(func=None):
    return calculate(8, func)


def nine(func=None):
    return calculate(9, func)


def plus(right):
    return lambda left: left + right


def minus(right):
    return lambda left: left - right


def times(right):
    return lambda left: left * right


def divided_by(right):
    return lambda left: left // right  # Integer division


def calculate(left, func):
    if func:
        return func(left)  # Closure
    return left


print(seven(times(five())))  # 35
print(four(plus(nine())))  # 13
print(eight(minus(three())))  # 5
print(six(divided_by(two())))  # 3
