def compute(x: int, y: int) -> int:
    return x * y // 2

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
