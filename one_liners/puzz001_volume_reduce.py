# x, y, z = input().strip().split()  # unpacking input str is: "x y z", for ex: "10 20 30"
# x, y, z = map(int, input().strip().split())
# volume = x * y * z
from functools import reduce

volume = reduce(lambda x, y: x * y, map(int, input().strip().split()))

print(volume)
