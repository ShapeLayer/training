def compute(a: int, b: int) -> int:
    return min(a // 2, b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(compute(a, b))
