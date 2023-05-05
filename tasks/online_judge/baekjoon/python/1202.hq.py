from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

def compute(n: int, k: int, jewels: list[tuple[int]], bags: list[int]) -> int:
    result: int = 0
    targets: list[tuple[int]] = []
    for bag in bags:
        while jewels and bag >= jewels[0][0]:
            heappush(targets, -(heappop(jewels)[1]))
        if targets:
            result += heappop(targets)
        elif not jewels:
            break
    return -result

if __name__ == '__main__':
    n, k = map(int, input().split())
    jewels: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    bags: list[int] = [int(input()) for _i in range(k)]
    jewels.sort()
    bags.sort()
    print(compute(n, k, jewels, bags))
