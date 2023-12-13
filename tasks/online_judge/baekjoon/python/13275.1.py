from sys import stdin
input = stdin.readline

def compute(gets: str) -> int:
    l, r = 0, -1
    n = len(gets)
    dp = [0 for i in range(n)]

    for i in range(n):
        size = -1
        if i > r:
            size = 1
        else:
            size = min(r - i + 1, dp[l + r - i])

        while i - size >= 0 and i + size < n and gets[i - size] == gets[i + size]:
            size += 1
            
        dp[i] = size
        size -= 1
        if i + size > r:
            l = i - size
            r = i + size
    return max(dp) - 1

if __name__ == '__main__':
    print(compute('#' + '#'.join(input().strip()) + '#'))
