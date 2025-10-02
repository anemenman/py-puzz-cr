def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    else:
        fib_list = [1, 1]  # first 2
        while len(fib_list) < n:
            next_fib = fib_list[-1] + fib_list[-2]  # Sum of 2 last
            fib_list.append(next_fib)
        return fib_list


print(fibonacci_iterative(100))
