n = int(input())
gets = input()

cycles = [
    'ABC',
    'BABC',
    'CCAABB'
]
counts = [0, 0, 0]

for i in range(n):
    for j in range(3):
        each = cycles[j]
        if gets[i] == each[i % len(each)]:
            counts[j] += 1

_max = max(counts)
print(_max)
if _max == counts[0]:
    print('Adrian')
if _max == counts[1]:
    print('Bruno')
if _max == counts[2]:
    print('Goran')
