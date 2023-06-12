def compute(a: float, b: float) -> float:
    return 1 / (1 + 10 ** ((b - a) / 400))

if __name__ == '__main__':
    a, b = map(float, input().split())
    print(compute(a, b))
