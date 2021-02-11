import sys
from math import trunc

n = int(sys.stdin.readline().rstrip())
p = n
c = 0
while True:
    if p < 10:
        p = p*10+p
    else:
        t = trunc(p/10)
        p = (p%10)*10 + ((t + p%10)%10)
    c += 1
    if p == n:
        break

print(c)