def compute(a: int, b: int) -> bool:
    days = a + 7 * b
    return 1 <= days <= 30

if __name__ == '__main__':
    a, b = int(input()), int(input())
    print(int(compute(a, b)))
