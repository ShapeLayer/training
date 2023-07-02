def compute(g: int, p: int, t: int) -> int:
    res = p * t + 1 * g
    if g * p < res:
        return 1
    if g * p > res:
        return 2
    return 0

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
