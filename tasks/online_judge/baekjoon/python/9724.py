from sys import stdin
input = stdin.readline

def compute(a: int, b: int) -> int:
    res = 0
    for n in range(int(a ** (1 / 3)), int(b ** (1 / 3)) + 1):
        if a <= n ** 3 <= b:
            res += 1
    return res

if __name__ == '__main__':
    for t in range(int(input())):
        a, b = map(int, input().split())
        print(f'Case #{t + 1}: {compute(a, b)}')
