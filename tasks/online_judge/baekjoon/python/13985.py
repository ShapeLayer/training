def compute(a: int, b: int, c: int) -> bool:
    return c == a + b

if __name__ == '__main__':
    gets = input().split()
    a, b, c = int(gets[0]), int(gets[2]), int(gets[4])
    print('YES' if compute(a, b, c) else 'NO')
