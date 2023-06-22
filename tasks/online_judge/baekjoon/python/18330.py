def compute(n: int, k: int) -> int:
    x = min(k + 60, n)
    return x * 1500 + (n - x) * 3000

if __name__ == '__main__':
    n, k = int(input()), int(input())
    print(compute(n, k))
