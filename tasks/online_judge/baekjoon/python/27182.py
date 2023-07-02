def compute(n: int, m: int) -> int:
    if n >= 8:
        return n - 7
    return m + 7

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
