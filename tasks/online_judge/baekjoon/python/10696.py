from sys import stdin
input = stdin.readline

def compute(n: str, x: str) -> int:
    remainder: int = 0
    div = int(x)
    for each in n:
        remainder = (remainder * 10 + int(each)) % div
    return remainder

if __name__ == '__main__':
    for t in range(int(input())):
        n, x = input().split()
        print(f'Case {t + 1}: {compute(n, x)}')
