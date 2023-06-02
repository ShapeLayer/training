def compute(n: int) -> tuple[int]:
    p = 5 * n - 400
    r = (p != 100) - (p > 100) * 2
    return p, r

if __name__ == '__main__':
    n = int(input())
    print(*compute(n))
