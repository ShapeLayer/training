from sys import stdin
input = stdin.readline

n, a, b = map(int, input().split())
_map = [[*map(int, input().split())] for _i in range(n)]

is_happy = True
for i in range(n):
    if _map[a - 1][b - 1] < _map[a - 1][i]:
        is_happy = False
        break
for i in range(n):
    if _map[a - 1][b - 1] < _map[i][b - 1]:
        is_happy = False
        break

print('HAPPY' if is_happy else 'ANGRY')
