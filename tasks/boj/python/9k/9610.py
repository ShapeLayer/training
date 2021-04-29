from sys import stdin
dots = [0, 0, 0, 0, 0]
for i in range(int(stdin.readline())):
    x, y = list(map(int, stdin.readline().split()))
    if x > 0 and y > 0:
        dots[0] += 1
    elif x < 0 and y > 0:
        dots[1] += 1
    elif x < 0 and y < 0:
        dots[2] += 1
    elif x > 0 and y < 0:
        dots[3] += 1
    else:
        dots[4] += 1
print('''Q1: {}
Q2: {}
Q3: {}
Q4: {}
AXIS: {}
'''.format(dots[0], dots[1], dots[2], dots[3], dots[4]))