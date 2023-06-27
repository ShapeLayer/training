from math import acos, pi
from sys import stdin
input = stdin.readline

def ccw(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> int:
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

def calc_dist(x1: int, y1: int, x2: int, y2: int) -> float:
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5

def find_convex_hull(n: int, dots: list[tuple[int]]) -> list[tuple[int]]:
    dots.sort()
    
    lower_hull: list[tuple[int]] = []
    for i in range(n):
        while len(lower_hull) >= 2:
            if ccw(*lower_hull[-2], *lower_hull[-1], *dots[i]) > 0:
                break
            lower_hull.pop()
        lower_hull.append(dots[i])
    
    upper_hull: list[tuple[int]] = []
    for i in range(n - 1, -1, -1):
        while len(upper_hull) >= 2:
            if ccw(*upper_hull[-2], *upper_hull[-1], *dots[i]) > 0:
                break
            upper_hull.pop()
        upper_hull.append(dots[i])
    
    return lower_hull[:-1] + upper_hull[:-1]

def get_angle(x1: int, y1: int, x2: int, y2: int) -> float:
    inner: int = (x1 * x2) + (y1 * y2) # inner prod
    v1: int = x1 ** 2 + y1 ** 2
    v2: int = x2 ** 2 + y2 ** 2
    return acos(inner / (v1 * v2))

def compute(n: int, l: int, dots: list[tuple[int]]) -> float:
    hull: list[tuple[int]] = find_convex_hull(n, dots)
    hull_len = len(hull)
    length: float = 0
    for i in range(hull_len):
        prev, now, next = hull[(i - 1) % hull_len], hull[i], hull[(i + 1) % hull_len]
        length += calc_dist(*prev, *now)
        '''
        vectors: list[tuple[int]] = [(prev[0] - now[0], prev[1] - now[1]), (now[0] - next[0], now[1] - next[1])]
        angle = get_angle(*vectors[0], *vectors[1])
        length += angle * l
        '''
    # 모든 각의 합은 2*PI의 배수
    length += 2 * pi * l
    return length

if __name__ == '__main__':
    n, l = map(int, input().split())
    dots: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    print(round(compute(n, l, dots)))
