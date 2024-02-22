from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
q = deque()
gets = sorted([[*map(int, input().split())] for _i in range(n)])
count = 0
for each in gets:
    i, v = each
    while q:
        peek = q.pop()
        if peek == 0:
            break
        if peek > v:
            count += 1
        elif peek == v:
            break
        else:
            q.append(peek)
            break
    q.append(v)
while len(q):
    peek = q.pop()
    if peek == 0:
        break
    count += 1
print(count)
