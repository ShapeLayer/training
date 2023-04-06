from sys import stdin
c = int(stdin.readline())

for i in range(c):
    s = stdin.readline().split()
    n = int(s.pop(0))
    s = list(map(int, s))
    e = (sum(s) / n)
    o = 0
    for stu in s:
        if stu > e:
            o += 1
    print('{}%'.format(format(round((o/n)*100, 5), '.3f')))