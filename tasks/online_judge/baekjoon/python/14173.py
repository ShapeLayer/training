def compute(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int) -> int:
    return max(max(x2, x4) - min(x1, x3), max(y2, y4) - min(y1, y3)) ** 2

if __name__ == '__main__':
    print(compute(*map(int, input().split()), *map(int, input().split())))
