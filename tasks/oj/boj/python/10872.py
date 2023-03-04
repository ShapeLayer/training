from sys import stdin

n = int(stdin.readline())

def facto(t, s):
    s += 1
    t *= s
    if n == 0:
        print(1)
    elif n != s:
        facto(t, s)
    else:
        print(t)

facto(1, 0)