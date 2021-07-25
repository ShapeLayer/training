from sys import stdin

n, b, h, w = map(int, stdin.readline().split())
c = [] # candidates

for _ in range(h):
    p = int(stdin.readline())
    a = list(map(int, stdin.readline().split())) # available
    for d in a: # driven
        if d >= n:
            c += [p]
            break

if c:
    t = min(c)*n # total
    if t <= b:
        print(t)
    else:
        print('stay home')
else:
    print('stay home')
