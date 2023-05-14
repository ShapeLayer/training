from sys import stdin
input = stdin.readline

def compute(n: int) -> bool:
    n_sqr = str(n ** 2)
    return n_sqr[-len(str(n)):] == str(n)

if __name__ == '__main__':
    t = int(input())
    for _i in range(t):
        n = int(input())
        print('YES' if compute(n) else 'NO')
