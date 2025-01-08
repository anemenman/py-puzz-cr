from io import StringIO

# Create data stream with StringIO
buff = StringIO()
for i in range(100):
    buff.write(str(i))
res_str = buff.getvalue()
buff.close()

print(res_str)

print('-------bytearray:')
byte_arr = bytearray(b'Hello, ')
byte_arr.extend(b'world!')

print(byte_arr)
