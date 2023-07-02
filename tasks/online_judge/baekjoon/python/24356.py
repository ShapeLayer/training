def compute(t1: int, m1: int, t2: int, m2: int) -> int:
    calced = (t2 - t1) * 60 + (m2 - m1)
    return calced if calced >= 0 else calced + 1440

if __name__ == '__main__':
    result = compute(*map(int, input().split()))
    print(result, result // 30)
