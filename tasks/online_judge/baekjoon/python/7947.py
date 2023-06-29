def compute(n: int) -> int:
    if n / 10 - n // 10 >= .5:
        return n // 10 + 1
    return n // 10

if __name__ == '__main__':
    for _t in range(int(input())) :
        r, g, b = 0, 0, 0
        for _i in range(10):
            _r, _g, _b = map(int, input().split())
            r, g, b = r + _r, g + _g, b + _b
        print(compute(r), compute(g), compute(b))
