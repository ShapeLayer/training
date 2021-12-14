from sys import stdin, stdout

t = int(stdin.readline())
for i in range(t):
    r, s = stdin.readline().rstrip().split()
    r = int(r)
    for j in range(len(s)):
        for k in range(r):
            stdout.write(s[j])
    stdout.write('\n')