n = int(input())
scores = [0] * n
for i in range(n):
    a, d, g = map(int, input().split())
    scores[i] = a * (d + g) * (2 if a == d + g else 1)
print(max(scores))