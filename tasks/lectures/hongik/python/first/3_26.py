n = int(input('n을 입력하시오 : '))
for i in range(n):
    if i % 2 == 0:
        for j in range(i*n+1, (i+1)*n+1, 1):
            print('%2d' % j, end=' ')
        print()
    else:
        for j in range((i+1)*n, i*n, -1):
            print('%2d' % j, end=' ')
        print()