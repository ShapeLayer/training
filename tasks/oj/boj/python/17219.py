from sys import stdin
gets = stdin.readline
n, m = map(int, gets().split())
saves = {}
for _ in range(n):
    site, pw = gets().rstrip().split()
    saves[site] = pw
for _ in range(m):
    print(saves[gets().rstrip()])