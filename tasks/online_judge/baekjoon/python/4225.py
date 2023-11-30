from sys import stdin
from math import ceil
input = stdin.readline

def dis(ax: int, ay: int, bx: int, by: int) -> float:
    dx, dy = ax - bx, ay - by
    return (dx * dx + dy * dy) ** .5

def ccw(ax: int, ay: int, bx: int, by: int, cx: int, cy: int) -> list[list[int]]:
    return (ax * by + bx * cy + cx * ay) - (bx * ay + cx * by + ax * cy)

def compute(n: int, dots: list[list[int]]):
    def _get_hull():
        dots.sort()

        hull_lower: list[list[int]] = []
        for dot in dots:
            while len(hull_lower) > 1:
                if ccw(*hull_lower[-2], *hull_lower[-1], *dot) > 0:
                    break
                hull_lower.pop()
            hull_lower.append(dot)
        
        hull_upper: list[list[int]] = []
        for dot in dots[::-1]:
            while len(hull_upper) > 1:
                if ccw(*hull_upper[-2], *hull_upper[-1], *dot) > 0:
                    break
                hull_upper.pop()
            hull_upper.append(dot)
        
        return hull_upper[1:] + hull_lower[1:]

    hull = _get_hull()

    res = None
    _len = len(hull)
    for i in range(_len):
        prev, now = hull[i], hull[(i + 1) % _len]
        _dis = dis(*prev, *now)
        cache = None
        for y, x in hull:
            if (x == prev[0] and y == prev[1]) or (x == now[0] and y == now[1]):
                continue
            _d = abs(ccw(*prev, *now, y, x) / _dis)
            cache = _d if not cache else _d if _d > cache else cache
        prev = now
        res = cache if not res else res if cache > res else cache
    return res

if __name__ == '__main__':
    i = 0
    while True:
        i += 1
        n = int(input())
        if not n:
            break
        dots = [[*map(int, input().split())] for _i in range(n)]
        print('Case %i: %.2f' % (i, ceil(compute(n, dots) * 100) / 100))
