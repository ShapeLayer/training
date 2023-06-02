def compute(n: int, a: int, b: int, c: int, d: int) -> int:
    return min(
        (n // a + (1 if n % a else 0)) * b,
        (n // c + (1 if n % c else 0)) * d
    )

if __name__ == '__main__':
    n, a, b, c, d = map(int, input().split())
    print(compute(n, a, b, c, d))
