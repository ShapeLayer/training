from sys import stdin
from collections import defaultdict
input = stdin.readline

scores = defaultdict(int)
while True:
    gets = input().strip()
    if gets == '-1':
        break
    t, prob, result = gets.split()
    t = int(t)
    if result == 'right':
        scores[prob] = -scores[prob] + t
    else:
        scores[prob] -= 20

print(sum([1 if scores[key] > 0 else 0 for key in scores]), sum([max(0, scores[key]) for key in scores]))
