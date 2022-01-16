n = int(input())
for i in range(n):
    body = ''
    for j in range(n):
        if i <= j:
            body += '*'
        else:
            body += ' '
    for j in range(n-1):
        if i+j < n-1:
            body += '*'
    print(body)