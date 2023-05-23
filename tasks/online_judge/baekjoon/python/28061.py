def compute(n: int, lemons: list[int]) -> int:
    result = 0
    for i in range(n):
        now = lemons[i] - (n - i)
        if now > result:
            result = now
    return result

if __name__ == '__main__':
    n = int(input())
    lemons: list[int] = list(map(int, input().split()))
    print(compute(n, lemons))
