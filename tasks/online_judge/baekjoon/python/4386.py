from sys import stdin
input = stdin.readline

def compute(n: int, stars: list[tuple[float]]) -> int:
    
    parents: list[int] = [i for i in range(n + 1)]
    
    def calc_distances() -> list[list[float]]:
        distances = []
        for i in range(n):
            for j in range(i):
                distance: float = ((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) ** 0.5
                distances.append((distance, i, j))
            distances.sort()
        return distances
    
    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa < pb:
            parents[pb] = pa
        else:
            parents[pa] = pb

    def find(n: int) -> int:
        if parents[n] == n:
            return n
        p = find(parents[n])
        parents[n] = p
        return p

    dists = calc_distances()
    costs: float = 0.0
    for dist in dists:
        cost, a, b = dist
        if find(a) != find(b):
            merge(a, b)
            costs += cost

    return costs

if __name__ == '__main__':
    n: int = int(input())
    stars: list[tuple[float]] = [tuple(map(float, input().split())) for _i in range(n)]
    print(compute(n, stars))
