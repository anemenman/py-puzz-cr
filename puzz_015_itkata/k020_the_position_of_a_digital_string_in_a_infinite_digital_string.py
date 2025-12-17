"""
Description:
There is a infinite string. You can imagine it's a combination of numbers from 1 to n, like this:

"123456789101112131415....n-2n-1n"
Please note: the length of the string is infinite. It depends on how long you need it(I can't offer it as a argument,
it only exists in your imagination) ;-)
Your task is complete function findPosition that accept a digital string num. Returns the position(index) of the
digital string(the first appearance).

For example:

findPosition("456") == 3
because "123456789101112131415".indexOf("456") = 3
            ^^^
Is it simple? No, It is more difficult than you think ;-)

findPosition("454") = ?
Oh, no! There is no "454" in "123456789101112131415",
so we should return -1?
No, I said, this is a string of infinite length.
We need to increase the length of the string to find "454"

findPosition("454") == 79
because "123456789101112131415...44454647".indexOf("454")=79
                                   ^^^
The length of argument num is 2 to 15. So now there are two ways: one is to create a huge own string to find the index
position; Or thinking about an algorithm to calculate the index position.

Which way would you choose? ;-)

Some examples:
 findPosition("456") == 3
 ("...3456...")
       ^^^
 findPosition("454") == 79
 ("...444546...")
        ^^^
 findPosition("455") == 98
 ("...545556...")
       ^^^
 findPosition("910") == 8
 ("...7891011...")
        ^^^
 findPosition("9100") == 188
 ("...9899100101...")
         ^^^^
 findPosition("99100") == 187
 ("...9899100101...")
        ^^^^^
 findPosition("00101") == 190
 ("...99100101...")
         ^^^^^
 findPosition("001") == 190
 ("...9899100101...")
           ^^^
 findPosition("123456789") == 0
 findPosition("1234567891") == 0
 findPosition("123456798") == 1000000071
A bit difficulty, A bit of fun, happy coding ;-)
"""

# def find_position(num):
#     num = str(num)
#     indexes = []
#
#     for step in range(0, len(num) + 1):
#         for start in range(0, step):
#             index = try_to_parse(num, start, step)
#             if index >= 0:
#                 indexes.append(index)
#
#     if not len(indexes):
#         return int(get_total_length(int('1' + num)) + 1)
#
#     return int(min(indexes))
#
#
# def try_to_parse(num, start, step):
#     if start + step <= len(num):
#         n = int(num[start:(start + step)])
#     else:
#         p1 = num[start:]
#         p2 = num[0:start]
#         common = len(p1) + len(p2) - step
#
#         chs = p2[common:]
#         if chs == '9' * len(chs):
#             p1 += '0' * len(chs)
#             n = int(p1)
#         else:
#             p1 = p1 + p2[common:]
#             n = int(p1) + 1
#         if str(n - 1)[(step - len(p2)):] != p2:
#             return -1
#
#     tokens = []
#     lena = 0
#
#     if start:
#         prev = str(n - 1)
#         tokens.append(prev[(len(prev) - start):])
#         lena += start
#
#     x = n
#     while lena < len(num):
#         stra = str(x)
#         if len(stra) + lena > len(num):
#             tokens.append(stra[0:(len(num) - lena)])
#             lena += len(num) - lena
#         else:
#             tokens.append(stra)
#             lena += len(stra)
#         x += 1
#
#     if ''.join(tokens) == num:
#         total = get_total_length(n)
#         return total - start
#     else:
#         return -1
#
#
# def get_total_length(n):
#     total: int = 0
#     lena = 1
#     x = 10
#
#     while n > x:
#         total += lena * (x - x / 10)
#         x *= 10
#         lena += 1
#
#     total += lena * (n - x / 10)
#     return total

from itertools import count


def num_index(n):
    if n < 10:
        return n - 1
    c = 0
    for i in count(1):
        c += i * 9 * 10 ** (i - 1)
        if n < 10 ** (i + 1):
            return c + (i + 1) * (n - 10 ** i)


def find_position(s):
    if not int(s):
        return num_index(int('1' + s)) + 1
    for j in range(1, len(s) + 1):
        poss = []
        for i in range(0, j + 1):
            sdt = s[0:j - i]
            end = s[j - i:j]
            for c in ([end + sdt, str(int(end) - 1) + sdt] if end and int(end) != 0 else [end + sdt]):
                if c[0] == '0':
                    continue
                ds = c
                n = int(c)
                while len(ds) < len(s) + j:
                    n += 1
                    ds += str(n)
                idx = ds.find(s)
                if idx != -1:
                    poss.append(num_index(int(c)) + idx)
        if len(poss) > 0:
            return min(poss)


assert find_position("456") == 3
assert find_position("454") == 79
assert find_position("455") == 98
assert find_position("910") == 8
assert find_position("9100") == 188
assert find_position("99100") == 187
assert find_position("00101") == 190
assert find_position("001") == 190
assert find_position("00") == 190
assert find_position("123456789") == 0
assert find_position("1234567891") == 0
assert find_position("123456798") == 1000000071
assert find_position("10") == 9
assert find_position("53635") == 13034
assert find_position("040") == 1091
assert find_position("11") == 11
assert find_position("99") == 168
assert find_position("667") == 122
assert find_position("0404") == 15050
assert find_position("949225100") == 382689688
assert find_position("58257860625") == 24674951477
assert find_position("3999589058124") == 6957586376885
assert find_position("555899959741198") == 1686722738828503
assert find_position("01") == 10
assert find_position("091") == 170
assert find_position("0910") == 2927
assert find_position("0991") == 2617
assert find_position("09910") == 2617
assert find_position("09991") == 35286
