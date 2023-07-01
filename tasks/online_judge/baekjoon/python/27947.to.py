from sys import stdin
from collections import deque
input = stdin.readline

def ccw(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> float:
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

def find_hull(dots: list[tuple[int]]) -> list[tuple[int]]:
    dots.sort()
    n = len(dots)

    lower_hull: deque = deque()
    for i in range(n):
        while len(lower_hull) >= 2:
            if ccw(*lower_hull[-2], *lower_hull[-1], *dots[i]) > 0:
                break
            lower_hull.pop()
        lower_hull.append(dots[i])
    
    upper_hull: deque = deque()
    for i in range(n - 1, -1, -1):
        while len(upper_hull) >= 2:
            if ccw(*upper_hull[-2], *upper_hull[-1], *dots[i]) > 0:
                break
            upper_hull.pop()
        upper_hull.append(dots[i])
    
    return list(lower_hull)[1:] + list(upper_hull)[1:]

def is_in_hull(dot: tuple[int], hull: list[tuple[int]]) -> bool:
    n = len(hull)
    prev = None
    for i in range(n):
        now = ccw(*dot, *hull[i], *hull[(i + 1) % n])
        if prev == None:
            prev = now
            continue
        if prev != now:
            return False
    return True

def calc_area(dots: list[tuple[int]]) -> float:
    area: int = 0
    n = len(dots)
    for i in range(n):
        area += dots[i % n][0] * dots[(i + 1) % n][1]
        area -= dots[(i + 1) % n][0] * dots[i % n][1]
    return area

def compute(n: int, a: int, starts: list[tuple[int]], queries: list[tuple[int]]) -> bool:
    a *= 2
    dots: list[tuple[int]] = starts
    is_wapas: bool = True
    prev_hull: list[tuple[int]] = find_hull(dots)
    for query in queries:
        if is_in_hull(query, prev_hull):
            continue
        dots.append(query)
        hull: list[tuple[int]] = find_hull(dots)
        now_area: float = calc_area(hull)
        if now_area >= a:
            return is_wapas
        is_wapas = not is_wapas
        prev_hull = hull
    return None

if __name__ == '__main__':
    n, a = map(int, input().split())
    starts: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(3)]
    queries: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    result = compute(n, a, starts, queries)
    if result == None:
        print('draw')
    else:
        print('wapas' if result else 'wider')
