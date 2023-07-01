def compute(a: int, b: int, c: int) -> tuple[int]:
    return 229 * 324 * a * 2, 297 * 420 * b * 2 ,210 * 297 * c 

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print('%.6f' % (sum(compute(a, b, c)) * .000001))
