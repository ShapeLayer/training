def compute(ds: int, dm: int, ys: int, ym: int) -> int:
    sun, moon = ys - ds, ym - dm
    while sun != moon:
        if sun < moon:
            sun += ys
        else:
            moon += ym
    return sun

if __name__ == '__main__':
    ds, ys = map(int, input().split())
    dm, ym = map(int, input().split())
    print(compute(ds, dm, ys, ym))
