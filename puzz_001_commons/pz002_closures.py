def fun1(x):
    # outer function that takes an argument 'x'
    def fun2(y):
        # inner function that takes an argument 'y'
        return x ** y  # 'x' is captured from the outer function

    return fun2  # Returning the inner function as a closure


# create a closure by calling outer_function
f = fun1(2)

# we can use the closure, which "remembers" the value of 'x' as 2
print(f(5))
print(f(20))
