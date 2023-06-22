from sys import stdin
input = stdin.readline

def compute(l: int, w: int, h: int, v: int) -> tuple[int]:
    if l == 0:
        l = v // w // h
    if w == 0:
        w = v // l // h
    if h == 0:
        h = v // l // w
    if v == 0:
        v = l * w * h
    return l, w, h, v

if __name__ == '__main__':
    while True:
        l, w, h, v = map(int, input().split())
        if l == w == h == v == 0:
            break
        print(*compute(l, w, h, v))
