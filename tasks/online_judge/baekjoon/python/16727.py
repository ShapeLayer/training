def compute(p1: int, p2: int, s1: int, s2: int) -> str:
    p = p1 + p2
    s = s1 + s2
    if p == s:
        if p1 == s2:
            return 'Penalty'
        elif p1 > s2:
            return 'Esteghlal'
        else:
            return 'Persepolis'
    elif p > s:
        return 'Persepolis'
    else:
        return 'Esteghlal'

if __name__ == '__main__':
    p1, s1 = map(int, input().split())
    s2, p2 = map(int, input().split())
    print(compute(p1, p2, s1, s2))
