def compute(a: int, b: int, c: int, d: int, e: int, f: int) -> tuple[int]:
    for i in range(-999, 1000):
        for j in range(-999, 1000):
            if a * i + b * j == c and d * i + e * j == f:
                return (i, j)

if __name__ == '__main__':
    a, b, c, d, e, f = map(int, input().split())
    print(*compute(a, b, c, d, e, f))
