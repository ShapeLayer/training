from math import ceil
from sys import stdin
input = stdin.readline

def ccw(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> int:
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

def find_convex_hull(n: int, dots: list[int]) -> list[tuple[int]]:
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
    
    return upper_hull[1:] + lower_hull[1:]

def compute(n: int, dots: list[tuple[int]]) -> list[str]:
    dots.sort()
    result = find_convex_hull(n, dots)[::-1]
    length = len(result)
    pivot_x, pivot_y, pivot_idx = int(1e10), int(-1e10), -1
    for i in range(length):
        if pivot_y < result[i][1]:
            pivot_x, pivot_y = result[i]
            pivot_idx = i
        elif pivot_y == result[i][1] and pivot_x > result[i][0]:
            pivot_x, pivot_y = result[i]
            pivot_idx = i
    result = result[pivot_idx:length] + result[0:pivot_idx]

    # build string
    buf = [str(length)]
    for each in result:
        buf.append(' '.join(map(str, each)))
    return buf

if __name__ == '__main__':
    for _t in range(int(input())):
        n = int(input())
        dots: list[tuple[int]] = []
        for _i in range(ceil(n / 5)):
            gets = list(map(int, input().split()))
            for i in range(0, len(gets), 2):
                dots.append((gets[i], gets[i + 1]))
        print('\n'.join(compute(n, dots)))
