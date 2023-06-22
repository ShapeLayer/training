from sys import stdin
input = stdin.readline

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)

def compute(a: int, b: int) -> int:
    return a * b // gcd(a, b)

if __name__ == '__main__':
    for _t in range(int(input())):
        a, b = map(int, input().split())
        print(compute(a, b))
