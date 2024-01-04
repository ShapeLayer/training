from sys import stdin
from math import ceil
input = stdin.readline

n, k = map(int, input().split())
students = [[0 for _i in range(2)] for _j in range(7)]
for _i in range(n):
    s, y = map(int, input().split())
    students[y][s] += 1
req = 0
for i in range(1, 7):
    for j in range(2):
        req += ceil(students[i][j]/k)
print(req)
