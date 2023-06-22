from sys import stdin
input = stdin.readline

def compute(n: int, m: int, k: int, pos: list[tuple[int]]) -> int:
    first_class = -1
    min_dist = int(1e10)
    for i in range(k):
        y, x = pos[i]
        dist = (y - 1) + ((m + 1) - x)
        if min_dist > dist:
            min_dist = dist
            first_class = i + 1
    return first_class

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    pos: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(k)]
    print(compute(n, m, k, pos))
