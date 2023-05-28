from sys import stdin
input = stdin.readline

def compute(n: int, m: int) -> tuple[int]:
    lost = m * 2 - n
    t = m - lost
    return lost, t

if __name__ == '__main__':
    t = int(input())
    for _i in range(t):
        n, m = map(int, input().split())
        print(*compute(n, m))
