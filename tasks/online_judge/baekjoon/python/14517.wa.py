# 문제 풀이 자체가 잘못됨
# 부분 수열이 연속하지 않아도 됨

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
    print(dp)
    return sum(map(lambda each: each // 2, dp))

if __name__ == '__main__':
    print(compute('#' + '#'.join(input().strip()) + '#'))
