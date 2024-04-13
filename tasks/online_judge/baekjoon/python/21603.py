n, k = map(int, input().split())

f = lambda x: x % 10

fk = f(k)
f2k = (2 * k) % 10

res = []
for i in range(n):
    fx = f(i + 1)
    if fx != f(k) and fx != f(2 * k):
        res.append(i + 1)

print(len(res))
print(' '.join(map(str, res)))
