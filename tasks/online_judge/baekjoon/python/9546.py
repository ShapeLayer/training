from sys import stdin
input = stdin.readline

def compute(n: int) -> int:
    return 2 ** n - 1

if __name__ == '__main__':
    for _t in range(int(input())):
        n = int(input())
        print(compute(n))
