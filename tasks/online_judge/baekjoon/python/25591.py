def compute(x: int, y: int) -> tuple[int]:
    a = 100 - x
    b = 100 - y
    c = 100 - (a + b)
    d = a * b
    q = d // 100
    r = d % 100
    return a, b, c, d, q, r

if __name__ == '__main__':
    x, y = map(int, input().split())
    a, b, c, d, q, r = compute(x, y)
    print(a, b, c, d, q, r)
    print(c + q, r)
