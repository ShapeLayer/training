from math import ceil

def compute(g: int, c: int, e: int) -> int:
    return max(ceil((e - c) * ((g - 1) * 2 + 1)), 0)

if __name__ == '__main__':
    for _i in range(int(input())):
        print(compute(*map(int, input().split())))
