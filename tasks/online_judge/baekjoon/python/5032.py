def compute(e: int, f: int, c: int) -> int:
    drinks = 0
    b = e + f
    while b >= c:
        drinks += b // c
        b = b // c + b % c
    return drinks

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
