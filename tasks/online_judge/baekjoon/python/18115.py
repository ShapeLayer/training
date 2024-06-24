from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
gets = [*map(int, input().split())]

q = deque()
for i in range(1, n + 1):
    now = gets.pop()
    if now == 1:
        q.appendleft(i)
    elif now == 2:
        q.insert(1, i)
    elif now == 3:
        q.append(i)

print(*q)
