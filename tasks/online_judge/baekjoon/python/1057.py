def compute(a: int, b: int) -> int:
    cnt = 0
    while a != b:
        a -= a // 2
        b -= b // 2
        cnt += 1
    return cnt

if __name__ == '__main__':
    n, a, b = map(int, input().split())
    print(compute(a, b))
