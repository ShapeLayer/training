from sys import stdin
import heapq
input = stdin.readline

def compute(arr: list[list[int]]):
    prev, _max = [], 0
    heapq.heappush(prev, 0)
    for i, s, e in arr:
        able = heapq.heappop(prev)
        if able > s:
            heapq.heappush(prev, able)
        heapq.heappush(prev, e)
        _max = max(_max, len(prev))
    return _max

if __name__ == '__main__':
    n = int(input())
    gets = sorted([[*map(int, input().split())] for _i in range(n)], key=lambda each: (each[1], each[2]))
    print(compute(gets))
