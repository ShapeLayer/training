import heapq
from sys import stdin
input = stdin.readline

def compute(n: int, queries: list[tuple[int]]) -> list[int]:
    result: list[int] = []
    presents: list[int] = []
    for query in queries:
        if query[0] == 0:
            if presents:
                result.append(-heapq.heappop(presents))
            else:
                result.append(-1)
        else:
            for i in range(1, query[0] + 1):
                heapq.heappush(presents, -query[i])
    return result

if __name__ == '__main__':
    n = int(input())
    queries: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    for each in compute(n, queries):
        print(each)
