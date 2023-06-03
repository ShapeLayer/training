def compute(a1: int, a2: int, a3: int) -> int:
    return min(a2 * 2 + a3 * 4, a1 * 2 + a3 * 2, a1 * 4 + a2 * 2)

if __name__ == '__main__':
    print(compute(int(input()), int(input()), int(input())))
