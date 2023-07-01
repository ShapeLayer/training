def compute(n: int, d: list[int]) -> float:
    if n % 2 == 0:
        return (d[n // 2 - 1] + d[(n // 2)]) / 2
    return d[(n + 1) // 2 - 1]

if __name__ == '__main__':
    i = 1
    while True:
        gets: list[int] = list(map(int, input().split()))
        if gets[0] == 0:
            break
        print('Case %d: %.1f' % (i, compute(gets[0], gets[1:])))
        i += 1
