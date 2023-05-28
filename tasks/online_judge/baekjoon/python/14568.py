def compute(n: int) -> int:
    s = 0
    for i in range(2, n - 1, 2):
        s += (n - i - 2) // 2
    return s

if __name__ == '__main__':
    n = int(input())
    print(compute(n))
