def compute(n: int) -> int:
    i = 1
    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n = n // 2
        i += 1
    return i

if __name__ == '__main__':
    n = int(input())
    print(compute(n))
