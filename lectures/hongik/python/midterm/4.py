n = float(input('1보다 작고 0보다 큰 소수를 입력하세요 : '))

def unit_fraction(frac: float):
    loop_cnt = 2
    b, a = 0, 0
    while True:
        b, a = 1/(loop_cnt-1), 1/loop_cnt # Before, After
        if frac < b and frac >= a:
            break
        loop_cnt += 1
    near = min(b - frac, frac - a)
    if near == b - frac:
        return b, loop_cnt - 1
    else:
        return a, loop_cnt

res, lower = unit_fraction(n)
print('가장 가까운 단위 분수는 1/{}이며 이 값은 {}'.format(lower, res))