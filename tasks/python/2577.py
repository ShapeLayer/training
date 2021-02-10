from sys import stdin
a = int(stdin.readline())
b = int(stdin.readline())
c = int(stdin.readline())

numcount = [0 for i in range(10)]

r = a*b*c
is_zero = True

for i in range(9):
    tc = 10**(9-(i+1))
    j = r//(tc)
    if is_zero and j != 0:
        is_zero = False
    elif is_zero:
        continue
    r = r - j * tc
    numcount[j] += 1

for num in numcount:
    print(num)