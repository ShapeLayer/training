from sys import stdin
from collections import deque
input = stdin.readline

dt = ((0, 1), (1, 0))

def compute(n: int, grid: list):
    vals = [[0 for _i in range(n + 1)] for _j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            vals[i][j] = max(vals[i][j - 1], vals[i - 1][j]) * 2 + grid[i - 1][j - 1]
    return vals[n][n]

if __name__ == '__main__':
    n = int(input())
    grid = [[*map(int, input().split())] for _i in range(n)]
    print(compute(n, grid))
