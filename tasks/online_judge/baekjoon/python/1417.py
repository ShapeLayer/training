import heapq
from sys import stdin
input = stdin.readline

def compute(n: int, votes: list[int]) -> int:
    if n == 1:
        return 0
    now = votes[0]
    diff = 0
    queue: list[int] = []
    for each in votes[1:]:
        heapq.heappush(queue, -each)
    while True:
        pop = -heapq.heappop(queue)
        if now > pop:
            break
        now += 1
        diff += 1
        heapq.heappush(queue, -(pop - 1))
    return diff

if __name__ == '__main__':
    n = int(input())
    votes: list[list[int]] = [int(input()) for i in range(n)]
    print(compute(n, votes))
