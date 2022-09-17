from collections import Counter
arr = []
for _i in range(10):
    arr += [int(input())]
c = dict(Counter(arr))
print(int(sum(arr)/10))
mx = max(c.values())
for key in c:
    if mx == c[key]:
        print(key)
        break