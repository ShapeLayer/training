def compute(a: int, b: int, c: int) -> int:
    return -a + c

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
