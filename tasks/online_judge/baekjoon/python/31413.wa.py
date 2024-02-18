from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
gains = [*map(int, input().split())]
total = sum(gains)
a, d = map(int, input().split())
invest = []
for i in range(d, n + 1):
    invest.append((sum(gains[i - d:i]), i - d))
for i in range(d):
    invest.append((sum(gains[n - d + i:n]), n - d + i))
invest.sort(reverse=True)

print(invest)

done = [False for _i in range(n)]
count = 0
while invest and m > total:
    now, start = invest.pop()
    if now >= a:
        break
    print(done)
    if True in done[start:min(start + d, n)]:
        continue
    total += a - now
    count += 1
    for i in range(start, min(start + d, n)):
        done[i] = True

print(done, total, invest)
print(count if m <= total else -1)
