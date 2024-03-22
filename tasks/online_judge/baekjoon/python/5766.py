from sys import stdin
from collections import defaultdict
input = stdin.readline

if __name__ == '__main__':
    while True:
        n, m = map(int, input().split())
        if n == m == 0:
            break
        _table = defaultdict(int)
        for _i in range(n):
            for each in map(int, input().split()):
                _table[each] += 1
        table = dict(_table)
        vals = sorted(table.values(), reverse=True)
        vals.pop(0)
        target = vals.pop(0)
        res = []
        for each in table:
            if table[each] == target:
                res.append(each)
        print(' '.join(map(str, sorted(res))))
    