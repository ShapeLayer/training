from sys import stdin
input = stdin.readline

def compute(d: float) -> float:
    w = 16 * d / (337 ** .5)
    h = w * 9 / 16
    return w, h

if __name__ == '__main__':
    while True:
        d, resh, resv = map(float, input().split())
        if d == resh == resv == 0:
            break
        w, h = compute(d)
        print('Horizontal DPI: %.2f' % (resh / w))
        print('Vertical DPI: %.2f' % (resv / h))
