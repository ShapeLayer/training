def compute(n: int) -> int:
    elapsed = 0
    i = 1
    while n > 0:
        n -= i
        i += 1
        if n - i < 0:
            i = 1
        elapsed += 1
    return elapsed

if __name__ == '__main__':
    n = int(input())
    print(compute(n))
