from collections import Counter
d = dict(Counter(bin(int(input()))[2:]))
if '1' in d and d['1'] == 1:
    print(1)
else:
    print(0)
