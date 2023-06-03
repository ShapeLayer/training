def compute(n: int, m: int) -> bool:
    return n == m

if __name__ == '__main__':
    print(int(compute(*map(int, input().split()))))
