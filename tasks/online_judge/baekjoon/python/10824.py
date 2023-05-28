def compute(a: str, b: str, c: str, d: str) -> int:
    e, f = int(a + b), int(c + d)
    return e + f

if __name__ == '__main__':
    a, b, c, d = input().split()
    print(compute(a, b, c, d))
