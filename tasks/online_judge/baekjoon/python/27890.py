def compute(x: int, n: int) -> int:
    for _i in range(n):
        if x % 2 == 0:
            x = (x // 2) ^ 6
        else:
            x = (2 * x) ^ 6
    return x

if __name__ == '__main__':
    x, n = map(int, input().split())
    print(compute(x, n))
