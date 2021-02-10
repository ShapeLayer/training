from sys import stdin
n, m = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))

max_ = 0
ml = len(c)-2
for i in range(ml):
    for j in range(ml - i):
        for k in range(ml - i - j):
            s = c[i] + c[i+j+1] + c[i+j+k+2]
            if m - s >= 0 and m - s < m - max_:
                max_ = s
print(max_)