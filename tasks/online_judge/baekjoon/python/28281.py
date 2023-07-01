def compute(n: int, x: int, an: list[int]) -> int:
    min_value = sum(an[0:2])
    for i in range(1, n - 1):
        now = sum(an[i:i+2])
        if min_value > now:
            min_value = now
    return min_value * x

if __name__ == '__main__':
    n, x = map(int, input().split())
    an = list(map(int, input().split()))
    print(compute(n, x, an))
