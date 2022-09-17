def rev(x: int) -> int:
    y = 0
    while x:
        y *= 10
        y += x % 10
        x //= 10
    return y

x, y = map(int, input().split())
print(rev(rev(x) + rev(y)))
