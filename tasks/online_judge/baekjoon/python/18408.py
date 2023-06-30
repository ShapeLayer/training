def compute(a: int, b: int, c: int) -> int:
    if a + b + c > 4:
        return 2
    return 1

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(compute(a, b, c))
