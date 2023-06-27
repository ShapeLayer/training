from sys import stdin
input = stdin.readline

def compute(n: float, s: str) -> str:
    if s == 'kg':
        return '%.4f lb' % (n * 2.2046)
    elif s == 'lb':
        return '%.4f kg' % (n * 0.4536)
    elif s == 'l':
        return '%.4f g' % (n * 0.2642)
    elif s == 'g':
        return '%.4f l' % (n * 3.7854)

if __name__ == '__main__':
    for _t in range(int(input())):
        n, s = input().split()
        print(compute(float(n), s))
