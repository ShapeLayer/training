from sys import stdin
input = stdin.readline

def check(full, short):
    ps = 0
    ls = len(short)
    for char in full:
        if char == short[ps]:
            ps += 1
            if ls == ps:
                return True
    if ls == ps:
        return True
    return False

t = int(input())
for i in range(t):
    n = int(input())
    names = [input().strip() for _i in range(n)]
    short = input().strip().upper()
    print(f'Data Set {i + 1}:')
    for name in names:
        if check(name.upper(), short):
            print(name)
