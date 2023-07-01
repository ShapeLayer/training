from sys import stdin
input = stdin.readline

def compute(n: int, vals: list[int]) -> int:
    return sorted(vals)[-n]

if __name__ == '__main__':
    n = int(input())
    vals: list[int] = sum([list(map(int, input().split())) for _i in range(n)], [])
    print(compute(n, vals))
