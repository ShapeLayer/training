from sys import stdin
input = stdin.readline
dt = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def compute(n: int, paint: list[str]):
    normal = [i for i in range(n * n)]
    weak = [i for i in range(n * n)]

    def find(parents: list[int], n: int) -> int:
        if n == parents[n]: return n
        parents[n] = find(parents, parents[n])
        return parents[n]

    def merge(parents: list[int], a: int, b: int):
        pa, pb = find(parents, a), find(parents, b)
        if pa > pb:
            parents[pb] = pa
            parents[b] = pa
        else:
            parents[pa] = pb
            parents[a] = pb

    for i in range(n):
        for j in range(n):
            pa_n = find(normal, i * n + j)
            pa_w = find(weak, i * n + j)
            for dy, dx in dt:
                ny, nx = i + dy, j + dx
                if 0 <= ny < n and 0 <= nx < n:
                    pb_n = find(normal, ny * n + nx)
                    pb_w = find(weak, ny * n + nx)
                    if paint[i][j] == paint[ny][nx]:
                        if pa_n != pb_n:
                            merge(normal, i * n + j, ny * n + nx)
                        if pa_w != pb_w:
                            merge(weak, i * n + j, ny * n + nx)
                    else:
                        if pa_w != pb_w:
                            if paint[i][j] in 'RG' and paint[ny][nx] in 'RG':
                                merge(weak, i * n + j, ny * n + nx)
    set_n, set_w = set(), set()
    for i in range(n * n):
        fn = find(normal, i)
        fw = find(weak, i)
        if fn not in set_n:
            set_n.add(fn)
        if fw not in set_w:
            set_w.add(fw)
    return len(set_n), len(set_w)

if __name__ == '__main__':
    n = int(input())
    paint = [input().strip() for _i in range(n)]
    print(*compute(n, paint))
