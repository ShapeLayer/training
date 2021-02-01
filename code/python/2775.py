from sys import stdin

t = int(stdin.readline())
for a in range(t):
    k = int(stdin.readline())
    n = int(stdin.readline())
    apt = [[0 for l in range(n)] for j in range(k)]
    for i in range(len(apt)+1):
        if i == 0:
            for j in range(n):
                apt[i][j] = j + 1
        elif i == k:
            print(sum(apt[i-1]))
        else:
            for j in range(n):
                apt[i][j] = sum(apt[i-1][0:j+1])