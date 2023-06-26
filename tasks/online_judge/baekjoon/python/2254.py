from sys import stdin
input = stdin.readline

def ccw(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> int:
    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3

def gen_hull(dots: list[tuple[int]]) -> list[tuple[int]]:
    dots.sort()

    hull_lower: list[tuple[int]] = []
    # 볼록껍질의 아래 파트
    for dot in dots:
        while len(hull_lower) > 1:
            if ccw(*hull_lower[-2], *hull_lower[-1], *dot) > 0:
                break
            hull_lower.pop()
        hull_lower.append(dot)

    # 볼록껍질의 위 파트
    hull_upper: list[tuple[int]] = []
    for dot in dots[::-1]:
        while len(hull_upper) > 1:
            if ccw(*hull_upper[-2], *hull_upper[-1], *dot) > 0:
                break
            hull_upper.pop()
        hull_upper.append(dot)

    return hull_lower[:-1] + hull_upper[:-1]

def is_in_hull(target: tuple[int], hull: list[tuple[int]]) -> bool:
    ln = len(hull)
    _dir = None
    for i in range(ln):
        p, q = hull[i % ln], hull[(i + 1) % ln]
        now_dir = ccw(*p, *q, *target) > 0
        if _dir == None:
            _dir = now_dir
        if now_dir != _dir:
            return False
    return True

def compute(n: int, target: tuple[int], dots: list[tuple[int]]) -> int:
    total = 0
    while len(dots) > 2:
        hull = gen_hull(dots)
        if is_in_hull(target, hull):
            total += 1
            dots = list(set(dots) - set(hull))
        else:
            break
    return total

if __name__ == '__main__':
    n, px, py = map(int, input().split())
    dots: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    target = (px, py)
    print(compute(n, target, dots))
