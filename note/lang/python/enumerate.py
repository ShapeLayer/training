## iterable: 반복 가능
## iterator: iterator 객체 자료형 -- iter()로 사용 가능
## iterable 요소로 enumerate 사용 가능

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
