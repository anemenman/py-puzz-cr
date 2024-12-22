text = 'Python 1234567890'

sliced_text = slice(6)
print(text[sliced_text])

numbers1 = [i for i in range(2, 99, 2)]
print(numbers1)

numbers2 = list(range(2, 99, 2))
numbers2.append(99)
print(numbers2)


def chunk(in_list, size):
    if size <= 0:
        raise ValueError(f'in_list must be greater than zero {size}')
    in_list_copy = in_list.copy()
    result = []
    last_chunk = []
    while in_list_copy:
        if len(last_chunk) == size:
            result.append(last_chunk)
            last_chunk = []
        last_chunk.append(in_list_copy[0])
        del in_list_copy[0]

    return result


def chunk_slice(in_list, size):
    print("--->")
    print(list(range(0, len(in_list), size)))
    return [in_list[i:i + size] for i in range(0, len(in_list), size)]


chunk_res = chunk(numbers2, 3)
print(chunk_res)

chunk_res2 = chunk_slice(numbers2, 3)
print("--->chunk_res2")
print(chunk_res2)


def check_chunk_negative():
    try:
        res = chunk(numbers2, -1)
    except ValueError:
        pass
    else:
        assert False


check_chunk_negative()


def sq_first_two_chunk(chunks):
    i = 2
    if len(chunks) < 2:
        i = len(chunks)
    for j in range(i):
        chunks[j] = [k ** 2 for k in chunks[j]]

    return chunks


def copy_pow_first_two_chunk(chunks, pow_value):
    chunks_result = chunks.copy()
    i = 2
    if len(chunks_result) < 2:
        i = len(chunks_result)
    for j in range(i):
        chunks_result[j] = [pow(k, pow_value) for k in chunks_result[j]]

    return chunks_result


def merge_chunks(chunks):
    res = []
    for chunk1 in chunks:
        res.extend(chunk1)

    return res


chunk_res3 = sq_first_two_chunk(chunk_res2)
print(chunk_res3)
res3 = merge_chunks(chunk_res3)
print(res3)

chunk_res_pow_1_2 = copy_pow_first_two_chunk(chunk_res2, 1 / 2)
chunk_res_pow_1_3 = copy_pow_first_two_chunk(chunk_res2, 1 / 3)

print("--->1/2")
print(chunk_res_pow_1_2)

print("--->1/3")
print(chunk_res_pow_1_3)
