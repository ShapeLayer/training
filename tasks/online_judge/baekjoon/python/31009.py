from sys import stdin
import heapq
input = stdin.readline

n = int(input())
jinju = -1
gets = []
for _i in range(n):
    d, c = input().split()
    c = int(c)
    if d == 'jinju':
        jinju = c
    heapq.heappush(gets, c)
while gets:
    n = heapq.heappop(gets)
    if n > jinju:
        heapq.heappush(gets, n)
        break

print(jinju)
print(len(gets))
