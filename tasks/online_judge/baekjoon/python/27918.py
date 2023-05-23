from sys import stdin
input = stdin.readline

def compute(n: int, opers: list[str]) -> tuple[int]:
    d, p = 0, 0
    for oper in opers:
        if oper == 'D':
            d += 1
        else:
            p += 1
        if abs(d - p) > 1:
            return d, p
    return d, p

if __name__ == '__main__':
    n = int(input())
    opers: list[str] = [input().strip() for _i in range(n)]
    d, p = compute(n, opers)
    print(f'{d}:{p}')
