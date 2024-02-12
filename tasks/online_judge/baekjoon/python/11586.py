from sys import stdin
input = stdin.readline

gets = [input().strip() for _j in range(int(input()))]
k = int(input())
v = -1 if k == 3 else 1
h = -1 if k == 2 else 1
for row in gets[::v]:
    print(row[::h])
