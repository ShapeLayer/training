import sys
t = int(sys.stdin.readline())

body = ''
for i in range(t):
    for j in range(t-i-1):
        body += ' '
    for j in range(i+1):
        body += '*'
    if i != (t-1):
        body += '\n'

print(body)