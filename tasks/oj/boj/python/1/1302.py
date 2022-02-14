from collections import Counter
sells = []
for _ in range(int(input())):
    sells += [input()]
c = dict(Counter(sells))
m = max(c.values())
bestsellers = []
for book in c:
    if c[book] == m:
        bestsellers += [book]
print(sorted(bestsellers)[0])