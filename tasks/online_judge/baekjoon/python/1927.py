import heapq
from sys import stdin
input = stdin.readline

if __name__ == '__main__':
  hq = []
  for _i in range(int(input())):
    x = int(input())
    if x == 0:
      if not hq:
        print(0)
      else:
        print(heapq.heappop(hq))
    else:
      heapq.heappush(hq, x)
