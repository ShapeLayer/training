from sys import stdin, stdout

t = int(stdin.readline())
for i in range(t):
    a, b = list(map(int, stdin.readline().split()))
    stdout.write(str(a+b)+'\n')