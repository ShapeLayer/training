import heapq
from sys import stdin
input = stdin.readline

def compute(r: int, c: int, gets: list[str]):
    done = [False for _i in range(9)]
    q = []
    for i in range(r):
        for j in range(c - 2):
            if gets[i][c - j - 2] != '.':
                n = int(gets[i][c - j - 2])
                if done[n - 1]:
                    continue
                done[n - 1] = True
                heapq.heappush(q, (j, n))
    prev = -1
    peekrank = 0
    result = [-1 for _i in range(9)]
    while q:
        pos, i = heapq.heappop(q)
        if prev != pos:
            peekrank += 1
        result[i - 1] = peekrank
        prev = pos
    return result

r, c = map(int, input().split())
gets = [input().strip() for _i in range(r)]
for each in compute(r, c, gets):
    print(each)
