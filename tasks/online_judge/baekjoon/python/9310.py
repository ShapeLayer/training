def compute(a: int, b: int, c: int) -> int:
    if b - a == c - b:
        d = b - a
        return (n * (2 * a + (n - 1) * d)) // 2
    if b / a == c / b:
        r = b // a
        return a * (r ** n - 1) // (r - 1)

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        a, b, c = map(int, input().split())
        print(compute(a, b, c))
