from sys import stdin
input = stdin.readline

def compute(n: int, x: int, k: int, swaps: list[tuple[int]]) -> int:
    for swap in swaps:
        a, b = swap
        if a == x: x = b
        elif b == x: x = a
    return x

if __name__ == '__main__':
    n, x, k = map(int, input().split())
    swaps: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(k)]
    print(compute(n, x, k, swaps))
