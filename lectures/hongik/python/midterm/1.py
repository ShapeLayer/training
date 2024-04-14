from sys import stdout
n = int(input('도형의 크기 n을 입력하시오 : '))
for i in range(n):
    for j in range(n):
        if i + j < n:
            stdout.write('*')
        else:
            stdout.write(' ')
    for j in range(n-1):
        if i <= j+1:
            stdout.write('*')
        else:
            stdout.write(' ')
    stdout.write('\n')
for i in range(n-1):
    for j in range(n-1):
        if i+2 > j:
            stdout.write('*')
        else:
            stdout.write(' ')
    for j in range(n):
        if i + j > n-3:
            stdout.write('*')
        else:
            stdout.write(' ')
    stdout.write('\n')