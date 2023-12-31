from sys import stdin
input = stdin.readline

a, b = map(int, input().split())
k, x = map(int, input().split())

val = min(k + x, b) - max(k - x, a) + 1
print(val if val > 0 else 'IMPOSSIBLE')
