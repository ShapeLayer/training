def compute(a: int, b: int) -> tuple[int]:
    return int(-a - (a * a - b) ** .5), int(-a + (a * a - b) ** .5)

if __name__ == '__main__':
    a, b = map(int, input().split())
    y, z = compute(a, b)
    if y == z:
        print(y)
    else:
        print(y, z)
