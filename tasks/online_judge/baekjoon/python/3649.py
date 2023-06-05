from sys import stdin
input = stdin.readline

def compute(x: int, n: int, legos: list[int]):
    legos.sort()
    lo, hi = 0, n - 1
    while lo < hi:
        if legos[lo] + legos[hi] > x:
            hi -= 1
        elif legos[lo] + legos[hi] < x:
            lo += 1
        else:
            return True, (legos[lo], legos[hi])
    return False, None

if __name__ == '__main__':
    gets = ''
    while True:
        try:
            gets = input()
        except EOFError:
            break
        gets = gets.strip()
        if not gets:
            break
        x = int(gets) * 10000000
        n = int(input())
        legos = [int(input()) for _i in range(n)]
        res, val = compute(x, n, legos)
        if res:
            print('yes', *val)
        else:
            print('danger')
