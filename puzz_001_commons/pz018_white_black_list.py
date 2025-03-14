"""OK - if at least 1 word is in the white list and each word not is in black list"""

white = ['white']
black = ['a', 'b', 'c']


def check(text):
    in_white = False

    for word in text.split():
        if word in black:
            return 'Error'
        if word in white:
            in_white = True
    if in_white:
        return 'Ok'
    return 'Error'


text1 = 'a f'
text2 = 'ab white'
text3 = 'a d white'
text4 = 'ab d black'

assert check(text1) == 'Error'
assert check(text2) == 'Ok'
assert check(text3) == 'Error'
assert check(text4) == 'Error'
