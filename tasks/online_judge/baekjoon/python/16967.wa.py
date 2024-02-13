from sys import stdin
input = stdin.readline

h, w, x, y = map(int, input().split())
gets = [[*map(int, input().split())] for _i in range(h + x)]

res = [each[:w] for each in gets[:h - x]] + [each[y:w + y] for each in gets[h:h + x]]
for each in res:
    print(*each)
