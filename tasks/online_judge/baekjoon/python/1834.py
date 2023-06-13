def compute(n: int) -> int:
    return sum([i for i in range(n + 1, n ** 2, n + 1)])

if __name__ == '__main__':
    print(compute(int(input())))
