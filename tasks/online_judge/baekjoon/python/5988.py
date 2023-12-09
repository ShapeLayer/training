from sys import stdin
input = stdin.readline

def compute(n: int) -> bool:
    return n % 2 == 1

if __name__ == '__main__':
    for _i in range(int(input())):
        print('odd' if compute(int(input())) else 'even')
