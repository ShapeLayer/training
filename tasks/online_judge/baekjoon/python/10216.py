from sys import stdin
input = stdin.readline

def compute(n: int, gets: list[int]):
    parents = [i for i in range(n)]

    def find(n: int) -> int:
        if n == parents[n]:
            return n
        parents[n] = find(parents[n])
        return parents[n]

    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa > pb:
            parents[pa] = pb
            parents[a] = pb
        elif pb > pa:
            parents[pb] = pa
            parents[b] = pa

    counts = n
    for i in range(n - 1):
        for j in range(i + 1, n):
            if find(i) != find(j):
                x1, y1, r1 = gets[i]
                x2, y2, r2 = gets[j]
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2:
                    merge(i, j)
                    counts -= 1
    return counts

if __name__ == '__main__':
    for _i in range(int(input())):
        n = int(input())
        gets = [[*map(int, input().split())] for _i in range(n)]
        print(compute(n, gets))

