from sys import stdin
for i in range(int(stdin.readline())):
    y, k = 0, 0
    for j in range(9):
        a, b = list(map(int, stdin.readline().split()))
        y += a
        k += b
    if y < k:
        print('Korea')
    elif y > k:
        print('Yonsei')
    else:
        print('Draw')