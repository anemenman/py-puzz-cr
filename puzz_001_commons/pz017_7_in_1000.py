"""How many numbers contain at least one digit 3 in the range from 1 to 1000?

Indeed, there is a way to do it much faster, that is, calculate all decimal numbers except 7.
You can determine the number of records that do not contain 3 by simply multiplying all the other
numbers 9 * 9 * 9 = 729. Accordingly, all that remains is to subtract the result obtained from
the total number 1000-729 = 271."""
import math

max_10 = 1000000
digits = int(math.log10(max_10))
no_count_7 = pow(9, digits)
count_7 = max_10 - no_count_7
print(f"Result : {count_7}")

count_verification = 0
for i in range(max_10 + 1):
    if '7' in str(i):
        count_verification += 1

print(f"Result verification: {count_verification}")
