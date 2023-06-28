from sys import stdin
input = stdin.readline

MAX = int(1e10)

def ccw(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> int:
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

def find_hull(hull: list[tuple[int]]) -> list[int]:
    hull.sort()
    ln = len(hull)

    lower_hull: list[tuple[int]] = []
    for i in range(ln):
        while len(lower_hull) >= 2:
            if ccw(*lower_hull[-2], *lower_hull[-1], *hull[i]) >= 0:
                break
            lower_hull.pop()
        lower_hull.append(hull[i])

    upper_hull: list[tuple[int]] = []
    for i in range(ln - 1, -1, -1):
        while len(upper_hull) >= 2:
            if ccw(*upper_hull[-2], *upper_hull[-1], *hull[i]) >= 0:
                break
            upper_hull.pop()
        upper_hull.append(hull[i])
    
    return lower_hull[1:] + upper_hull[1:]

def compute(hull: list[tuple[int]]) -> list[int]:
    hull_sorted = find_hull(hull)
    ln = len(hull_sorted)
    min_x, min_y, idx = MAX, MAX, -1
    for i in range(ln):
        x, y = hull_sorted[i]
        if min_x > x:
            min_x, min_y, idx = x, y, i
        elif min_x == x and min_y > y:
            min_x, min_y, idx = x, y, i
    hull_sorted = hull_sorted[idx:ln] + hull_sorted[0:idx]
    return hull_sorted

if __name__ == '__main__':
    n = int(input())
    hull: list[tuple[int]] = []
    for _i in range(n):
        x, y, c = input().split()
        if c == 'Y':
            hull.append((int(x), int(y)))
    result = compute(hull)
    print(len(result))
    for each in result:
        print(*each)
