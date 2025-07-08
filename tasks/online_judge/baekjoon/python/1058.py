from sys import stdin
input = stdin.readline

def compute(n: int, gets: list[str]):
    parents: list[int] = [i for i in range(n)]
    count: list[int] = [0 for _i in range(n)]

    def find(n: int) -> int:
        if parents[n] == n:
            return n
        parents[n] = find(parents[n])
        return parents[n]

    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa > pb:
            parents[pa] = pb
            parents[a] = pb
            count[pb] += count[pa] + 1
            count[pa] = 0
        elif pa < pb:
            parents[pb] = pa
            parents[b] = pa
            count[pa] += count[pb] + 1
            count[pb] = 0

    for i in range(n):
        for j in range(n):
            if gets[i][j] == 'Y':
                merge(i, j)

    return max(count)

if __name__ == '__main__':
    n = int(input())
    gets = [input().strip() for _i in range(n)]
    print(compute(n, gets))
