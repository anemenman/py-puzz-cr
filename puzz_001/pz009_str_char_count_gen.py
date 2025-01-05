# 'abbcc' -> 'a1b2c2'


def converter(text):
    return ''.join(i + str(text.count(i)) for i in sorted(set(text)))


res = converter("abbcc")
print(res)
print(set('wfafsfasffsadf'))
print(sorted(set('wfafsfasffsadf')))

print(i + '1' for i in set('text'))
