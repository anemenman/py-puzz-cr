def cache(func):
    data = {}

    def wrapper(*args):
        if args in data:
            print(f'-------->Use cache for {args}')
            return data[args]
        else:
            result = func(*args)
            data[args] = result
            return result

    return wrapper


@cache
def fibonacci(n):
    print(f'Calculate fibonacci of {n}')
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))  # Calculate fibonacci
print(fibonacci(10))  # Use cache
