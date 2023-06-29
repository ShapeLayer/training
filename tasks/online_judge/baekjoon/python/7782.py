def compute(b1: int, b2: int, a: int, b: int, c: int, d: int) -> bool:
    return a <= b1 and c >= b1 and b <= b2 and d >= b2

if __name__ == '__main__':
    n = int(input())
    b1, b2 = map(int, input().split())
    for _t in range(n):
        a, b, c, d = map(int, input().split())
        if compute(b1, b2, a, b, c, d):
            print('Yes')
            exit()
    print('No')
