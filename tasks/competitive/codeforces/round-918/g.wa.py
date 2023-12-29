from sys import stdin
import heapq
from collections import defaultdict
input = stdin.readline

for _i in range(int(input())):
  n, m = map(int, input().split())
  p = [i for i in range(n + 1)]
  conn = [[*map(int, input().split())] for _i in range(m)]
  bikes = [0] + [*map(int, input().split())]
  c = []
  for each in conn:
    _from, _to, w = each
    c.append([_from, _to, w * bikes[_from]])
    c.append([_to, _from, w * bikes[_to]])
  start = 1
  graph = defaultdict(list)
  dist = defaultdict(list)
  q = [(0, start)]
  for v, w, d in c:
    graph[v].append([w, d])
  while q:
    cost, node = heapq.heappop(q)
    if node not in dist:
      dist[node] = cost
      for x, c in graph[node]:
        d = cost + c
        heapq.heappush(q, [d, x])
  print(dist[n])
