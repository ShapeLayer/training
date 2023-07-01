from sys import stdin
import heapq
input = stdin.readline

def compute(n: int, queries: list[int]) -> list[int]:
    queue: list[int] = []
    result: list[int] = []
    for query in queries:
        if query != 0:
            heapq.heappush(queue, -query)
        else:
            if not queue:
                result.append(0)
            else:
                result.append(-heapq.heappop(queue))
    return result

if __name__ == '__main__':
    n = int(input())
    queries: list[int] = [int(input()) for _i in range(n)]
    for each in compute(n, queries):
        print(each)
