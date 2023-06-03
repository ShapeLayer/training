def compute(gets: list[int]) -> int:
    if gets[-3] - gets[-2] == gets[-2] - gets[-1]:
        return gets[-1] + gets[-1] - gets[-2]
    return gets[-1] * (gets[-1] // gets[-2])

if __name__ == '__main__':
    n = int(input())
    gets: list[int] = [int(input()) for _i in range(n)]
    print(compute(gets))
