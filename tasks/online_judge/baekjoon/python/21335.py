from math import pi

def compute(n: int) -> float:
    return (n / pi) ** 0.5 * 2 * pi

if __name__ == '__main__':
    n = int(input())
    print(compute(n))
