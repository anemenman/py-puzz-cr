def fib_next():
    a, b = 0, 1

    def res():
        # The nonlocal keyword is used to work with variables inside nested functions,
        # where the variable should not belong to the inner function.
        # Use the keyword nonlocal to declare that the variable is not local.
        nonlocal a, b
        a, b = b, a + b
        return a

    return res


f = fib_next()
for i in range(10):
    print(f())
