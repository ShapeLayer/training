def compute(x: float) -> float:
    return 100.0 / ((1.609344 / 3.785411784) * x)

if __name__ == '__main__':
    x = float(input())
    print('%.6f' % compute(x))
