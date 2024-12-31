def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


# n = 1000 #RecursionError: maximum recursion depth exceeded in comparison
n = 100
result = factorial(n)
print(f'The factorial of {n}: {result}')
