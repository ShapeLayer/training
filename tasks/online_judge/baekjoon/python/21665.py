from sys import stdin
input = stdin.readline

def compute(n: int, m: int, origin: list[str], other: list[str]) -> int:
    match = 0
    for i in range(n):
        for j in range(m):
            if origin[i][j] == other[i][j]:
                match += 1
    return match

if __name__ == '__main__':
    n, m = map(int, input().split())
    origin: list[str] = [input().strip() for _i in range(n)]
    input()
    other: list[str] = [input().strip() for _i in range(n)]
    print(compute(n, m, origin, other))
