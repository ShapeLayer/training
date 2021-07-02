dic = {
    'a': 3,
    'b': 5,
    'c': 8,
    'd': 11
}

for i in enumerate(dic):
    print(i[0], i)  # index (index, key)

for i, j in enumerate(dic):
    print(i, j)     # index key

for i, (j, k) in enumerate(dic.items()): # dict.items() => [(key, value), (key, value), ...]
    print(i, j, k)  # index key value
