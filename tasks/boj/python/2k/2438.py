import sys
t = int(sys.stdin.readline())

body = ''
for i in range(t):
    for j in range(i+1):
        body += '*'
    body += '\n'

print(body)