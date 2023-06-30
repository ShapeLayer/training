def compute(a: int, b: int, c: int) -> int:
    return sorted([a, b, c,])[1]

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
