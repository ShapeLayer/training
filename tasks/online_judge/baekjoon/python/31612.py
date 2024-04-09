from collections import Counter
_, c = input(), Counter(input())

res = 0
for key in c:
    if key == 'o':
        res += c[key]
    else:
        res += c[key] * 2

print(res)
