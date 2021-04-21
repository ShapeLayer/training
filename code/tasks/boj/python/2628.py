from sys import stdin
w, h = map(int, stdin.readline().split())
t = int(input())
line, delta = [[0, h], [0, w]], [[], []]
for _ in range(t):
    a, b = map(int, stdin.readline().split())
    if a == 0:
        line[0] += [b]
    else:
        line[1] += [b]
for i in range(len(line)):
    line[i].sort()
    for j in range(len(line[i])-1):
        delta[i] += [line[i][j+1] - line[i][j]]
size = []
for h in delta[0]:
    for v in delta[1]:
        size += [h*v]
print(max(size))