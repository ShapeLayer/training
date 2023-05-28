from sys import stdin
input = stdin.readline

def compute(n: int) -> str:
    return f'{n} {n}'

if __name__ == '__main__':
    t = int(input())
    for _i in range(t):
        print(compute(int(input())))
