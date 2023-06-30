def compute(k: int, n: int, queries: list[list[str]]) -> int:
    now = k - 1
    total: int = 0
    for time, is_true in queries:
        total += int(time)
        if total >= 210:
            return now + 1
        if is_true == 'T':
            now = (now + 1) % 8

if __name__ == '__main__':
    k = int(input())
    n = int(input())
    queries: list[list[str]] = [input().split() for _i in range(n)]
    print(compute(k, n, queries))
