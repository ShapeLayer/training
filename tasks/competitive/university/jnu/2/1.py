from collections import Counter
n, k = map(int, input().split())
home = list(map(int, input().split()))
c = dict(Counter(home))
target = min(c.values())
sums = 0
for cc in c:
	if c[cc] == target:
		sums += cc
print(sums)
