from sys import stdin
input = stdin.readline

loop = 1
while True:
    gets = [*map(int, input().split())]

    target = -1
    for i in range(3):
        if gets[i] == -1:
            target = i

    a, b, c = gets
    if a == b == c == 0:
        break
    
    result = None
    if target == 2:
        result = (a ** 2 + b ** 2) ** .5
    else:
        result = c ** 2 - sorted(gets)[1] ** 2
        if result < 0:
            result = None
            break
        else:
            result **= .5
    
    print(f'Triangle #{loop}')
    if result:
        print(['a', 'b', 'c'][target] + ' = %.03f' % result)
    else:
        print('Impossible.')
    print()
    loop += 1
