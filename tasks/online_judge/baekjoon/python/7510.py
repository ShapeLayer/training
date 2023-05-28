from sys import stdin
input = stdin.readline

def compute(a: int, b: int, c: int) -> bool:
    return c * c == a * a + b * b

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        a, b, c = sorted(map(int, input().split()))
        print(f'Scenario #{i}:')
        print('yes' if compute(a, b, c) else 'no')
        if i != n:
            print()
