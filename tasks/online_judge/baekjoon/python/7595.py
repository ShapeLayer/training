from sys import stdin
input = stdin.readline

def compute(n: int) -> str:
    buf: list[str] = []
    for i in range(1, n + 1):
        buf.append('*' * i)
    return '\n'.join(buf)

if __name__ == '__main__':
    n = -1
    while True:
        n = int(input())
        if n == 0:
            break
        print(compute(n))
