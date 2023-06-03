from sys import stdin
input = stdin.readline

def compute(w: int, h: int) -> str:
    buf: list[str] = ['X' * w for _j in range(h)]
    return '\n'.join(buf)

if __name__ == '__main__':
    for _t in range(int(input())):
        print(compute(*map(int, input().split())))
        print()
