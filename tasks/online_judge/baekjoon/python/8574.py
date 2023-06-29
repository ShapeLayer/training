from sys import stdin
input = stdin.readline

def compute(n: int, k: int, x: int, y: int, dots: list[tuple[int]]) -> int:
    result = 0
    for dot in dots:
        _x, _y = dot
        if ((_x - x) ** 2 + (_y - y) ** 2) ** 0.5 > k:
            result += 1
    return result

if __name__ == '__main__':
    n, k, x, y = map(int, input().split())
    dots: list[tuple[int]] = [tuple(map(int, input().split())) for _t in range(n)]
    print(compute(n, k, x, y, dots))
