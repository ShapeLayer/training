from sys import stdin
input = stdin.readline

a, b, c = map(int, input().split())
n = int(input())

max_score = -1
for _i in range(n):
    score = 0
    for j in range(3):
        x, y, z = map(int, input().split())
        score += a * x + b * y + c * z
    max_score = max(max_score, score)
print(max_score)
