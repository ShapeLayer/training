n = int(input())
for i in range(n):
    body = ''
    for j in range(n):
        if i+j >= n-1:
            body += '*'
        else:
            body += ' '
    for j in range(n-1):
        if i > j:
            body += '*'
    print(body)
for i in range(n-1):
    body = ''
    for j in range(n):
        if i <= j-1:
            body += '*'
        else:
            body += ' '
    for j in range(n-1):
        if i+j < n-2:
            body += '*'
    print(body)