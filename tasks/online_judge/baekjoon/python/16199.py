def compute(y1: int, m1: int, d1: int, y2: int, m2: int, d2: int) -> tuple[int]:
    if m1 < m2:
        int_age = y2 - y1
    elif m1 == m2 and d1 <= d2:
        int_age = y2 - y1
    else:
        int_age = y2 - y1 - 1
    kr_age = y2 - y1 + 1
    count_age = y2 - y1
    return int_age, kr_age, count_age

if __name__ == '__main__':
    y1, m1, d1 = map(int, input().split())
    y2, m2, d2 = map(int, input().split())
    for method in compute(y1, m1, d1, y2, m2, d2):
        print(method)
