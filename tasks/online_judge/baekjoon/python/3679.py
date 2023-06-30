from sys import stdin
input = stdin.readline

def ccw(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> int:
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

def find_hull(n: int, dots: list[tuple[int]]) -> list[tuple[int]]:
    dots.sort()

    lower_hull: list[tuple[int]] = []
    for i in range(n):
        while len(lower_hull) >= 2:
            if ccw(*lower_hull[-2][0:2], *lower_hull[-1][0:2], *dots[i][0:2]) >= 0:
                break
            lower_hull.pop()
        lower_hull.append(dots[i])
    
    upper_hull: list[tuple[int]] = []
    for i in range(n - 1, -1, -1):
        while len(upper_hull) >= 2:
            if ccw(*upper_hull[-2][0:2], *upper_hull[-1][0:2], *dots[i][0:2]) >= 0:
                break
            upper_hull.pop()
        upper_hull.append(dots[i])

    return lower_hull

def calc_dist(x1: int, y1: int, x2: int, y2: int) -> float:
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5

def compute(n: int, dots: list[tuple[int]]) -> list[tuple[int]]:
    hull: list[tuple[int]] = find_hull(n, dots.copy())

    remains: list[tuple[int]] = list(set(dots) - set(hull))
    remains.sort(key=lambda each: (each[0], each[1]), reverse=True)
    result = hull + remains
    return [each[2] for each in result]

if __name__ == '__main__':
    t = int(input())
    for _i in range(t):
        gets: list[int] = list(map(int, input().split()))
        n = gets[0]
        dots: list[tuple[int]] = [(gets[i * 2 + 1], gets[i * 2 + 2], i) for i in range(n)]
        print(*compute(n, dots))
