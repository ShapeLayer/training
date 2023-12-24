from sys import stdin
from collections import defaultdict
from math import floor
input = stdin.readline

def compute(n: int, m: int, q: int, c: dict, grp: dict, query: list[str]) -> list:
    buf = []
    gets = defaultdict(int)
    for oper in query:
        if oper[0] == '1':
            a, b = oper[1], int(oper[2])
            if c[a] * b <= m:
                m -= c[a] * b
                gets[a] += b
        elif oper[0] == '2':
            a, b = oper[1], int(oper[2])
            if b <= gets[a]:
                gets[a] -= b
                m += b * c[a]
        elif oper[0] == '3':
            a, _c = oper[1], int(oper[2])
            c[a] = max(c[a] + _c, 0)
        elif oper[0] == '4':
            d, _c = int(oper[1]), int(oper[2])
            for each in grp[d]:
                c[each] = max(c[each] + _c, 0)
        elif oper[0] == '5':
            d, e = int(oper[1]), int(oper[2])
            for each in grp[d]:
                c[each] = floor(c[each] * (100 + e) / 100)
                c[each] = c[each] - c[each] % 10
        elif oper[0] == '6':
            buf.append(m)
        elif oper[0] == '7':
            g = 0
            for each in gets:
                g += gets[each] * c[each]
            buf.append(m + g)
    return buf

if __name__ == '__main__':
    n, m, q = map(int, input().split())
    c, grp = {}, defaultdict(list)
    for _i in range(n):
        g, h, p = input().split()
        g, p = int(g), int(p)
        c[h] = p
        grp[g].append(h)
    query = [input().split() for _i in range(q)]
    print('\n'.join(map(str, (compute(n, m, q, c, grp, query)))))
