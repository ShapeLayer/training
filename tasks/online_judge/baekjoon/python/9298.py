from sys import stdin
input = stdin.readline

def compute(n: int, x: list[tuple[float]], y: list[tuple[float]]) -> tuple[float]:
    area, perimeter = 0, 0
    if n != 1:
        nx = x[-1][0] - x[0][0]
        ny = y[-1][1] - y[0][1]
        area = nx * ny
        perimeter = 2 * (nx + ny)
    return area, perimeter

if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        arr = [tuple(map(float, input().split())) for _i in range(n)]
        x, y = sorted(arr, key=lambda each: each[0]), sorted(arr, key=lambda each: each[1])
        area, perimeter = compute(n, x, y)
        print(f'Case {t + 1}: Area {area}, Perimeter {perimeter}')
