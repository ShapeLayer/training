def compute(ln: int) -> tuple[str]:
    o = 30 * 31
    c = chr(o)
    return c * ln, c * (ln - 2) + chr(o * 30 // 31) + chr(o * 2)

if __name__ == '__main__':
    # a = ''.join([chr(n // 31), chr(n % 31)])
    # b = chr(n)
    n = int(input())
    a, b = compute(n)
    print(a)
    print(b)
