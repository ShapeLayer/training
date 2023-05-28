from sys import stdin
input = stdin.readline

def compute(n: int) -> str:
    result: list[str] = []
    buf: list[str] = []
    for _i in range(n - 1):
        buf.append(' ')
    buf.append('*')
    result.append(''.join(buf))
    for i in range(2, n + 1):
        buf.clear()
        for _j in range(1, n - i + 1):
            buf.append(' ')
        buf.append('*')
        for _k in range(1, (i - 1) * 2):
            buf.append(' ')
        buf.append('*')
        result.append(''.join(buf))
    return '\n'.join(result)

if __name__ == '__main__':
    n = int(input())
    print(compute(n))
