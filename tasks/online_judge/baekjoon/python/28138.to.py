from sys import stdin
input = stdin.readline

def compute(n: int, k: int, pos: list[tuple[int]]):
    cnt = 0
    for i in range(n):
        for j in range(i):
            if i == j: continue
            ax, ay = pos[i]
            bx, by = pos[j]
            if ax == bx: continue
            if abs((ay - by) / (ax - bx)) == k:
                cnt += 1
    return cnt * 2

if __name__ == '__main__':
    n, k = map(int, input().split())
    pos: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    print(compute(n, k, pos))
