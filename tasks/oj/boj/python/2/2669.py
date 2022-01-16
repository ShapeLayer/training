from sys import stdin
space = {}

for _ in range(4):
    x, y = [0, 0], [0, 0]
    x1, y1, x2, y2 = list(map(int, stdin.readline().split()))
    x[0], x[1], y[0], y[1] = min([x1, x2]), max([x1, x2]), min([y1, y2]), max([y1, y2])
    for x_ in range(x[0], x[1]):
        try:
            space[x_]
        except KeyError:
            space[x_] = set()
        for y_ in range(y[0], y[1]):
            space[x_].add(y_)

cnt = 0
for k in space:
    cnt += len(space[k])
print(cnt)