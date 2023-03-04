from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    equa = stdin.readline().rstrip().split()
    n = 0
    for i in range(len(equa)):
        if i == 0:
            n = float(equa[i])
        elif equa[i] == '@':
            n *= 3
        elif equa[i] == '%':
            n += 5
        elif equa[i] == '#':
            n -= 7
    print(format(n, '.2f'))