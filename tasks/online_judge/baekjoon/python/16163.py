from sys import stdin
input = stdin.readline

def compute(gets: str):
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
        
        if dp[i]:
            if dp[i] & 1:
                count = count + dp[i] // 2 + 1
            else:
                count = count + dp[i] // 2
    
    return count

if __name__ == '__main__':
    print(compute('#' + '#'.join(input().strip()) + '#'))
