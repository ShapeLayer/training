from sys import stdin
input = stdin.readline

def compute(a: str, b: str) -> tuple[str]:
    return b, a

if __name__ == '__main__':
    for t in range(int(input())):
        a, b = compute(input().strip(), input().strip())
        print(f'Case {t + 1}: {a}, {b}')
