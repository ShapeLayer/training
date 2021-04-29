from sys import stdin
while True:
    ns = list(map(int, stdin.readline().split()))
    if ns == [0, 0, 0]:
        break
    c = max(ns)
    ab = 0
    for n in ns:
        if n != c:
            ab += n**2
    if ab == c**2:
        print('right')
    else:
        print('wrong')