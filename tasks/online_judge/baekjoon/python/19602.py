def compute(a: int, b: int, c: int) -> bool:
    return (a * 1 + b * 2 + c * 3) >= 10

if __name__ == '__main__':
    a, b, c = int(input()), int(input()), int(input())
    print('happy' if compute(a, b, c) else 'sad')
