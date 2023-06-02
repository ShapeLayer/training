def compute(n: int, m: int, k: int) -> int:
    return min(m, k) + n - max(m, k)

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    print(compute(n, m, k))
