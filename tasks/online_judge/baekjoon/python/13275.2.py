from sys import stdin
input = stdin.readline

def compute(gets: str) -> int:
    r, p = 0, 0
    n = len(gets)
    dp = [0 for i in range(n)]

    for i in range(n):
        if i <= r:
            dp[i] = min(dp[2 * p - i], r - i)
        size = dp[i]

        while i - size - 1 >= 0 and i + size + 1 < n and gets[i - size - 1] == gets[i + size + 1]:
            size += 1

        dp[i] = size

        if i + size > r:
            r = i + size
            p = i
    return max(dp)

if __name__ == '__main__':
    print(compute('#' + '#'.join(input().strip()) + '#'))
