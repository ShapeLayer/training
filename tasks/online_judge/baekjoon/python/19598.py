import heapq

def compute(n: int, timeline: list[tuple[int]]) -> int:
    timeline.sort()
    required: int = 0
    ends = []
    for each in timeline:
        start, end = each
        while ends:
            now = heapq.heappop(ends)
            if now > start:
                heapq.heappush(ends, now)
                break
        heapq.heappush(ends, end)
        required = max(required, len(ends))
    return required

if __name__ == '__main__':
    n: int = int(input())
    timeline: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    print(compute(n, timeline))
