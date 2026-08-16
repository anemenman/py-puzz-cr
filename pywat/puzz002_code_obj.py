def hello(name):
    return f"Hello, {name}"


print(hello.__code__)

print("Print compiled:")
import dis


def add(a, b):
    return a + b


dis.dis(add)

print("---------")
source = """
x = 10
y = 20
print(x + y)
"""

code = compile(source, filename="<string>", mode="exec")

exec(code)
