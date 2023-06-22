def compute(a: int, b: int, c: int) -> int:
    return max(b - a, c - b) - 1

if __name__ == '__main__':
    while True:
        try:
            a, b, c = map(int, input().split())
            print(compute(a, b, c))
        except:
            break
