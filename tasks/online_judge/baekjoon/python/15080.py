def compute(h1: int, m1: int, s1: int, h2: int, m2: int, s2: int) -> int:
    secs1 = h1 * 3600 + m1 * 60 + s1
    secs2 = h2 * 3600 + m2 * 60 + s2
    if secs1 > secs2:
        return secs2 - secs1 + 3600 * 24
    return secs2 - secs1

if __name__ == '__main__':
    t1 = map(int, input().split(':'))
    t2 = map(int, input().split(':'))
    print(compute(*t1, *t2))
