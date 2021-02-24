from sys import stdin
from collections import Counter
n, m = list(map(int, stdin.readline().split()))
never = [[], []] # [0] => never heard, [1] => never see
for _ in range(n):
    never[0] += [stdin.readline().rstrip()]
for _ in range(m):
    never[1] += [stdin.readline().rstrip()]
never[0].sort()
never[1].sort()
never_heard = Counter(never[0])
never_see = Counter(never[1])
arr = list(never_heard - (never_heard - never_see))
print(len(arr))
for name in arr:
    print(name)