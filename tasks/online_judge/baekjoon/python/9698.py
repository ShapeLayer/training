from sys import stdin
input = stdin.readline

def compute(h: int, m: int) -> tuple[int]:
    if m < 45:
        m += 15
        h = (h + 23) % 24
    else:
        m -= 45
    return h, m

if __name__ == '__main__':
    for i in range(1, int(input()) + 1) :
        h, m = map(int, input().split())
        print(f'Case #{i}:', *compute(h, m))
