from math import ceil

def compute(x: int, y: int) -> int:
    return ceil(((x * y) / 4840 ) / 5)

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
