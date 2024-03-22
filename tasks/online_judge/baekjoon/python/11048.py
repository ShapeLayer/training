from sys import stdin
input = stdin.readline

def compute(n, m, gets):
    gains = [[0 for _i in range(m)] for _j in range(n)]
    gains[0][0] = gets[0][0]
    for i in range(n):
        for j in range(m):
            for dy, dx in ((1, 0), (0, 1), (1, 1)):
                ny, nx = i + dy, j + dx
                if not (0 <= ny < n and 0 <= nx < m):
                    continue
                gains[ny][nx] = max(gains[ny][nx], gains[i][j] + gets[ny][nx])
    return gains[n - 1][m - 1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    gets = [[*map(int, input().split())] for _i in range(n)]
    print(compute(n, m, gets))
