from math import ceil

def compute(a: int, b: int, c: int) -> int:
    return ceil(a / c) * ceil(b / c)

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
