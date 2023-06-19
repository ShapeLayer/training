from sys import stdin
input = stdin.readline

def compute(y: float, x: float, d: float, w: float) -> bool:
    return (y > 56 or x > 45 or d > 25) and y + x + d > 125 or \
            w > 7

if __name__ == '__main__':
    count = 0
    for _t in range(int(input())):
        y, x, d, w = map(float, input().split())
        if compute(y, x, d, w):
            print(0)
        else:
            count += 1
            print(1)
    print(count)
