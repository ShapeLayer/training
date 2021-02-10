from sys import stdin

x = int(stdin.readline())

i = 0
s = 0
while True:
    i += 1
    s = i * (i + 1) /2
    if s >= x:
        break

a = int(s - x + 1)
b = int(i - (s - x))

if i % 2 == 1:
    print('{}/{}'.format(a, b))
else:
    print('{}/{}'.format(b, a))