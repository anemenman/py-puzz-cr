str_res1 = ''
for i in range(100):
    str_res1 += str(i)

print(str_res1)

print('----------')

str_res2 = []
for i in range(100):
    str_res2.append(str(i))

print('->'.join(str_res2))
