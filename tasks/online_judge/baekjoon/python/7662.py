import heapq
from collections import defaultdict
from sys import stdin
input = stdin.readline

def compute(n: int, queries: list[tuple]) -> tuple[int]:
    min_heap, max_heap = [], []
    min_deleted, max_deleted = defaultdict(lambda: 0), defaultdict(lambda: 0)

    for query in queries:
        oper, params = query
        if oper == 'D':
            if params == 1:
                while max_heap:
                    pop = -heapq.heappop(max_heap)
                    if min_deleted[pop]:
                        min_deleted[pop] -= 1
                    else:
                        max_deleted[pop] += 1
                        break
            else:
                while min_heap:
                    pop = heapq.heappop(min_heap)
                    if max_deleted[pop]:
                        max_deleted[pop] -= 1
                    else:
                        min_deleted[pop] += 1
                        break
        else:
            heapq.heappush(max_heap, -params)
            heapq.heappush(min_heap, params)
    queue = []

    for each in min_heap:
        if max_deleted[each] > 0:
            max_deleted[each] -= 1
        else:
            queue.append(each)

    if queue:
        return max(queue), min(queue)
    else:
        return None

if __name__ == '__main__':
    for _t in range(int(input())):
        n = int(input())
        queries: list[tuple] = []
        for _i in range(n):
            gets = input().split()
            queries.append((gets[0], int(gets[1])))
        result = compute(n, queries)
        if result == None:
            print('EMPTY')
        else:
            print(*result)
