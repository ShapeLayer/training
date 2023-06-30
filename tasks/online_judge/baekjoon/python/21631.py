def compute(a: int, b: int):
    if a >= b:
        return b
    return a + 1

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(compute(a, b))
