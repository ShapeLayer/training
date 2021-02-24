from sys import stdin

for _ in range(int(stdin.readline())):
    r, e, c = list(map(int, stdin.readline().split()))
    if r == e - c:
        print('does not matter')
    elif r > e - c:
        print('do not advertise')
    else:
        print('advertise')