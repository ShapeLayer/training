from sys import stdin
input = stdin.readline

def compute(N: int, K: int, coords: list):
    if K >= N:
        return 0
    
    coords.sort()
    
    dist = [coords[i] - coords[i - 1] for i in range(1, N)]
    dist.sort()

    for i in range(K - 1):
        dist.pop()
    
    return sum(dist)

if __name__ == "__main__":
    N = int(input())
    K = int(input())
    coords = [*map(int, input().split())]

    print(
        compute(N, K, coords)
    )
