from sys import stdin
input = stdin.readline

def compute(n: int, m: int, gets: list[int], q: list[list[int]]) -> list[int]:
    r, p = 0, 0
    n = len(gets)
    dp = [0 for i in range(n)]
    count = 0

    for i in range(n):
        if i <= r:
            dp[i] = min(dp[2 * p - i], r - i)
        size = dp[i]

        while i - size - 1 >= 0 and i + size + 1 < n and gets[i - size - 1] == gets[i + size + 1]:
            size = size + 1

        dp[i] = size

        if r < i + size:
            r = i + size
            p = i
    
    res = []
    for s, e in q:
        m = (s + e - 1)
        res.append(int(dp[m] >= e - s + 1))
    return res

if __name__ == '__main__':
    n = int(input())
    gets = [*map(int, input().split())]
    arr = [gets[i // 2] if i & 1 else -1 for i in range(2 * n + 1)]
    m = int(input())
    q = [[*map(int, input().split())] for _i in range(m)]
    for each in compute(2 * n + 1, m, arr, q):
        print(each)
