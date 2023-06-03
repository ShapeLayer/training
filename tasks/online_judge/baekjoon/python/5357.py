from sys import stdin
input = stdin.readline

def compute(gets: str) -> str:
    buf: list[str] = [gets[0]]
    prev = gets[0]
    for c in gets[1:]:
        if prev != c:
            buf.append(c)
            prev = c
    return ''.join(buf)

if __name__ == '__main__':
    n = int(input())
    for _t in range(n):
        print(compute(input().strip()))
