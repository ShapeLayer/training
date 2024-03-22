from sys import stdin
input = stdin.readline

dp = [1, 1, 1, 2, 2, 3]

def compute(n: int):
    ln = len(dp)
    if ln < n:
        for i in range(ln, n):
            dp.append(dp[i - 1] + dp[i - 5])
    return dp[n - 1]

if __name__ == '__main__':
    for _t in range(int(input())):
        print(compute(int(input())))
