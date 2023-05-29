def compute(n: int, t: int) -> tuple[int]:
    total = sum(t) + 8 * (n - 1)
    return total // 24, total % 24

if __name__ == '__main__':
    n = int(input())
    t: list[int] = list(map(int, input().split()))
    print(*compute(n, t))
