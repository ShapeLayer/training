from heapq import heappush, heappop

def compute(n: int, m: int, a: list):
    hq = []
    for each in a:
        heappush(hq, each)
    
    for _ in range(m):
        x = heappop(hq)
        y = heappop(hq)
        heappush(hq, x + y)
        heappush(hq, x + y)
    
    return sum(hq)

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [*map(int, input().split())]
    print(compute(n, m, a))
