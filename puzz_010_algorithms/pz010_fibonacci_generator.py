def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


gen = fibonacci_generator(10)
print(next(gen))

for i in gen:
    print(i)
