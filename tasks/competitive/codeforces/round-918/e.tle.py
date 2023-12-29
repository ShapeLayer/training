from sys import stdin
from collections import deque
input = stdin.readline

gets = []
a, b = [], []

def query(_type, init, fin):
  print(_type, init, fin)
  if _type == 0:
    i, j = init + int(init % 2 == 0), fin - int(fin % 2 == 0)
    if i == j or i + 1 == j:
      if i % 2 == 1:
        a[i][j] = gets[i]
      else:
        a[i][j] = 0
    else:
      m = (i + j) // 2
      a[i][j] = query(0, i, m) + query(0, m + 2, j)
    return a[i][j]
  else:
    i, j = init + int(init % 2 == 1), fin - int(fin % 2 == 1)
    if i == j:
      if i % 2 == 1:
        b[i][j] = 0
      else:
        b[i][j] = gets[i]
    else:
      m = (i + j) // 2
      b[i][j] = query(1, i, m) + query(1, m + 2, j)
    return b[i][j]

for _i in range(int(input())):
  n = int(input())
  gets = [*map(int, input().split())]
  a, b = [[None for _i in range(n)] for _j in range(n)], [[None for _i in range(n)] for _j in range(n)]
  l, r = 0, n - 1
  flag = False
  queue = deque()
  if query(0, l, r) == query(1, l, r):
    flag = True
  else:
    if l < r:
      queue.append((l + 1, r))
      queue.append((l, r - 1))
  while queue:
    l, r = queue.popleft()
    if query(0, l, r) == query(1, l, r):
      flag = True
      break
    else:
      if l < r:
        queue.append((l + 1, r))
        queue.append((l, r - 1))
  print('YES' if flag else 'NO')
