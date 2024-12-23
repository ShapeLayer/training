from sys import stdin
from collections import deque
input = stdin.readline

def compute(n: int, gets: list[int]) -> list[int]:
    _max = max(gets)
    buckets = [deque() for _ in range(10)]
    q = deque(gets)
    radix = 1
    while _max >= radix:
        while q:
            now = q.popleft()
            buckets[(now // radix) % 10].append(now)
        for bucket in buckets:
            while bucket:
                q.append(bucket.popleft())
        radix *= 10
    
    return list(q)

if __name__ == '__main__':
    n = int(input())
    gets = [int(input()) for _ in range(n)]
    print('\n'.join(map(str, compute(n, gets))))
