from sys import stdin
from math import ceil
x = int(stdin.readline())

res = ceil((-1 + (1 + 8*x)**0.5)/2)
if x == 1:
    sum_pre_res = 0
else:
    sum_pre_res = res * (res - 1) * 0.5

a, b = 0, res + 1
for i in range(x - int(sum_pre_res)):
    a += 1
    b -= 1

if res % 2 == 0:
    print('{}/{}'.format(a, b))
else:
    print('{}/{}'.format(b, a))