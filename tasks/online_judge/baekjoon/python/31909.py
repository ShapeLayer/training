n = int(input())
keys = [i for i in range(8)]
for each in map(int, input().split()):
    _bin = '{0:08b}'.format(each)
    if _bin.count('1') != 2:
        continue
    a = _bin.find('1')
    b = _bin.find('1', a + 1)
    keys[7 - a], keys[7 - b] = keys[7 - b], keys[7 - a]
k = int(input())
print(keys[k])
