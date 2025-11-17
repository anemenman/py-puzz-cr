"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be
rounded to the closest valid value.
Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""


def rgb(r, g, b):
    check_int(r)
    check_int(g)
    check_int(b)
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    return '{:02X}{:02X}{:02X}'.format(r, g, b)


def rgb2(*args):
    return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args))


def check_int(x):
    if not type(x).__name__ == 'int':  # python2 does not have instanceof()
        raise TypeError("given value is not of type int")


print(rgb(255, 255, 255))  # FFFFFF
print(rgb(255, 255, 300))  # FFFFFF
print(rgb(0, 0, 0))  # 000000
print(rgb(148, 0, 211))  # 9400D3
print(rgb('a', 0, 211))  # 9400D3
