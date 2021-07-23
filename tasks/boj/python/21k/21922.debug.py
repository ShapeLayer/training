from sys import argv
from random import choice, random
m, n = map(int, argv[1:3])
output = []
for _ in range(m):
    arr = []
    for __ in range(n):
        r = random()
        if r < 0.75:
            arr += [0]
        elif r < 0.95:
            arr += [choice((1, 2, 3, 4))]
        else:
            arr += [9]
    output += [arr]
for line in output:
    print(' '.join(list(map(str, line))))
