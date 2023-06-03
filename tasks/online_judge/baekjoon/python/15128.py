def compute(p1: int, q1: int, p2: int, q2: int) -> float:
    res = p1 / q1 * p2 / q2 / 2
    return 1 if int(res) == res else 0

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
