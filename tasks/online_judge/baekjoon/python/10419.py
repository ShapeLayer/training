def compute(d: int) -> int:
    i = 0
    while i + i * i <= d:
        i += 1
    return i - 1

if __name__ == '__main__':
    t = int(input())
    for _i in range(t):
        print(compute(int(input())))
