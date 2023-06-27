from sys import stdin
input = stdin.readline

def compute(a: int, b: int, wd: str) -> int:
    res = a - b if wd == 'W' else a + b
    return res if res >= -200 else None

if __name__ == '__main__':
    while True:
        a, wd, b = input().split()
        if a == b == '0':
            break
        res = compute(int(a), int(b), wd)
        if res:
            print(res)
        else:
            print('Not allowed')
