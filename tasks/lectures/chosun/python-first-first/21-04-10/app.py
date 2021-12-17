a, b = map(int, input().split())
if a+b > 10 or a < 0 or b < 0:
    print('Error!')
else:
    for i in range(1, a+1):
        body = ''
        for j in range(i):
            body += str(b+j)
        for j in range(a-i):
            body += '*'
        print(body)