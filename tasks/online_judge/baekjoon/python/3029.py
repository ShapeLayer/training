def compute(h1: int, m1: int, s1: int, h2: int, m2: int, s2: int) -> tuple[int]:
    sec1 = h1 * 60 * 60 + m1 * 60 + s1
    sec2 = h2 * 60 * 60 + m2 * 60 + s2
    time = (sec2 - sec1) % (24 * 60 * 60)
    if time == 0:
        return 24, 0, 0
    return time // 60 // 60, time // 60 % 60, time % 60

if __name__ == '__main__':
    time1 = map(int, input().split(':'))
    time2 = map(int, input().split(':'))
    h, m, s = compute(*time1, *time2)
    print('%02d:%02d:%02d' % (h, m, s))
