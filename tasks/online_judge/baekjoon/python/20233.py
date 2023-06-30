def compute(a: int, x: int, b: int, y: int, t: int) -> tuple[int]:
    return a + max(t - 30, 0) * x * 21, b + max(t - 45, 0) * y * 21

if __name__ == '__main__':
    a, x = int(input()), int(input())
    b, y = int(input()), int(input())
    t = int(input())
    print(*compute(a, x, b, y, t))
