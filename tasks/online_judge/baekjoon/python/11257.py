def compute(a: int, b: int, c: int, d: int) -> str:
    sums = b + c + d
    if sums < 55:
        return f'{a} {sums} FAIL'
    elif b / 35 < .3:
        return f'{a} {sums} FAIL'
    elif c / 25 < .3:
        return f'{a} {sums} FAIL'
    elif d / 40 < .3:
        return f'{a} {sums} FAIL'
    else:
        return f'{a} {sums} PASS'

if __name__ == '__main__':
    for _t in range(int(input())):
        print(compute(*map(int, input().split())))
