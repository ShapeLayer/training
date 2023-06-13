from sys import stdin
input = stdin.readline

def compute(a: int, b: str, c: int) -> bool:
    if b == '==':
        return a == c
    elif b == '!=':
        return a != c
    elif b == '>':
        return a > c
    elif b == '<':
        return a < c
    elif b == '>=':
        return a >= c
    elif b == '<=':
        return a <= c

if __name__ == '__main__':
    loops: int = 1
    while True:
        a, b, c = input().split()
        if b == 'E':
            break
        result = 'true' if compute(int(a), b, int(c)) else 'false'
        print(f'Case {loops}: {result}')
        loops += 1
