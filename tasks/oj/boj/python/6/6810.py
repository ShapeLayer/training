a, b = 1, 3
res = 0
for n in '9780921418' + input() + input() + input():
    res += int(n) * a
    a, b = b, a
print(f'The 1-3-sum is {res}')