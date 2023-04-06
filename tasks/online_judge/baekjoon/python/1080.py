from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
arrs = [[list(map(int, list(input().rstrip()))) for _i in range(n)] for _j in range(2)]
cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if arrs[0][i][j] != arrs[1][i][j]:
            cnt += 1
            for y in range(3):
                for x in range(3):
                    arrs[0][i+y][j+x] = (arrs[0][i+y][j+x] + 1) % 2

for i in range(n):
    for j in range(m):
        if arrs[0][i][j] != arrs[1][i][j]:
            print(-1)
            exit()
print(cnt)