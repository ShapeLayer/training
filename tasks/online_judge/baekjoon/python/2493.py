import heapq
from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
towers = deque([*map(int, input().split())])
result = [0 for _i in range(n)]
hq = []
i = n - 1
while towers:
    now = towers.pop()
    while hq:
        val, idx = heapq.heappop(hq)
        if now >= val:
            result[idx] = i + 1
        else:
            heapq.heappush(hq, (val, idx))
            break
    heapq.heappush(hq, (now, i))
    i -= 1
print(*result)
