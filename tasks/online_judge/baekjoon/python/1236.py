from sys import stdin
input = stdin.readline

def compute(n: int, m: int, gets: list[str]) -> int:
    vert, hori = [False for _i in range(n)], [False for _i in range(m)]
    for i in range(n):
        for j in range(m):
            if gets[i][j] == 'X':
                vert[i] = True
                hori[j] = True
    v, h = 0, 0
    for each in vert:
        if not each:
            v += 1
    for each in hori:
        if not each:
            h += 1
    return max(v, h)

if __name__ == '__main__':
    n, m = map(int, input().split())
    gets = [input().strip() for _i in range(n)]
    print(compute(n, m, gets))
