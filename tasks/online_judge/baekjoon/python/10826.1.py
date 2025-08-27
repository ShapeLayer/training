from sys import stdin, setrecursionlimit
setrecursionlimit(int(2e5))
input = stdin.readline

class Solution:
    def __init__(self, N: int):
        self.dp = [-1 for _i in range(N + 1)]
        self.dp[0] = 0
        self.dp[1] = 1

    def __call__(self, n: int) -> int:
        if self.dp[n] != -1:
            return self.dp[n]

        self.dp[n] = self(n - 1) + self(n - 2)
        return self.dp[n]

def compute(N: int) -> int:
    sol = Solution(N)
    return sol(N)

if __name__ == "__main__":
    N = int(input())
    print(compute(N))
