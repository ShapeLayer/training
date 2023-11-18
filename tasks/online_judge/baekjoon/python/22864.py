def compute(a: int, b: int, c: int, m: int):
    worked, tired = 0, 0
    for _i in range(24):
        if tired + a <= m:
            worked += b
            tired += a
        else:
            tired = max(0, tired - c)
    return worked

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
