def compute(a: int, b: int, c: int) -> int:
    return (b // a) * 3 * c

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(compute(a, b, c))
