def compute(a: int, b: int) -> int:
    return a if a == b else max(a, b)

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
