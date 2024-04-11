from sys import stdin
input = stdin.readline

for _t in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    x1, x2, x3, x4, y1, y2, y3, y4 = min(x1, x2), max(x1, x2), min(x3, x4), max(x3, x4), min(y1, y2), max(y1, y2), min(y3, y4), max(y3, y4)
    overlap = -1
    if x1 > x4 or y2 < y3 or x2 < x3 or y1 > y4:
        overlap = 0
    else:
        nx1, ny1, nx2, ny2 = max(x1, x3), max(y1, y3), min(x2, x4), min(y2, y4)
        overlap = (nx2 - nx1) * (ny2 - ny1)
    print(max(0, (x2 - x1) * (y2 - y1) - overlap))
