def compute(n: int, x: int, y: int) -> int:
    if n == 1:
        return 0
    if (x == 1 or x == n) or (y == 1 or y == n):
        if (x == 1 or x == n) and (y == 1 or y == n):
            return 2
        else:
            return 3
    else:
        return 4

if __name__ == '__main__':
    n = int(input())
    x, y = map(int, input().split())
    print(compute(n, x, y))
