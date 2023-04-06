from sys import stdin
m, n, d = map(int, stdin.readline().split())

def is_target(val): return str(d) in str(val)

cnt = 0
pl = [True for i in range(n+1)]
pl[0] = False
pl[1] = False
for i in range(2, n+1):
    if not pl[i]: continue
    if m <= i <= n:
        if is_target(i): cnt += 1
    for j in range(2, n//i+1):
        pl[i*j] = False

print(cnt)