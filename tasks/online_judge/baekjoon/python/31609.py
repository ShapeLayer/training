from collections import Counter
_, c = input(), Counter(map(int, input().split()))
for each in sorted(dict(c).keys()):
    print(each)
