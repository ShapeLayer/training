def compute(a: int, b: int) -> float:
    diag = (a * a + b * b) ** 0.5
    rect = a + b
    return rect - diag

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(compute(a, b))
