def compute(a: int, b: int) -> int:
    def case_compute(n: int) -> int:
        c = n % 4
        if c == 0: return n
        if c == 1: return n ^ (n - 1)
        if c == 2: return n ^ (n - 1) ^ (n - 2)
        if c == 3: return 0
    return case_compute(b) ^ case_compute(a - 1)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(compute(a, b))
