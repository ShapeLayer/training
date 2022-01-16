from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().rstrip().split()))
    cnt = 0
    for i in range(n, m+1):
        cnt += str(i).count('0')
    print(cnt)
