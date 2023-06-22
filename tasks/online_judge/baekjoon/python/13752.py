from sys import stdin
input = stdin.readline

def compute(n: int, vals: list[int]) -> list[str]:
    return ['=' * val for val in vals]

if __name__ == '__main__':
    n = int(input())
    vals: list[int] = [int(input()) for _t in range(n)]
    print('\n'.join(compute(n, vals)))
