from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
s = {}
for _i in range(n):
    s[input().strip()] = True
cnt = 0
for _i in range(m):
    if input().strip() in s:
        cnt += 1

print(cnt)
