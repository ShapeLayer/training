from sys import stdin

n, m = list(map(int, stdin.readline().split()))
dict_ = {}
nhs = [] # never heard and see

for _ in range(n):
    dict_[stdin.readline().rstrip()] = 1
for _ in range(m):
    try:
        name = stdin.readline().rstrip()
        dict_[name]
        nhs += [name]
    except KeyError:
        pass
nhs.sort()
print(len(nhs))
for name in nhs:
    print(name)