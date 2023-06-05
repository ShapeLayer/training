def compute(s: int, a: int, b: int) -> int:
    if s <= a:
        return 250
    return 250 + ((s - a) // b) * 100 + ((s - a) % b != 0) * 100

if __name__ == '__main__':
    s, a, b = int(input()), int(input()), int(input())
    print(compute(s, a, b))
