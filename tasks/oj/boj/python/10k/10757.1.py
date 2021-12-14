from sys import stdin
a, b = list(map(int, stdin.readline().split()))

def int_split(n):
    res = n % 1000000 # 백만으로 나눈 나머지 => 십만
    n = (n - res) // 1000000
    #print(res, n)
    if n < 0:
        n = 0
    return res, n

al, bl = [], []
while True:
    if a != 0:
        splited_a, a = int_split(a)
        al += [splited_a]
    if b != 0:
        splited_b, b = int_split(b)
        bl += [splited_b]
    if a == 0 and b == 0:
        break

cl = al

for i in range(len(bl)):
    if i < len(cl):
        cl[i] += bl[i]
        #print('{}: bl: {} cl: {}'.format(i, bl[i], cl[i]))
    else:
        cl += [bl[i]]

for i in range(len(cl)):
    i_calc = cl[i] // 1000000
    if i_calc != 0:
        if len(cl)-1 > i:
            cl[i+1] += i_calc
        else:
            cl += [i_calc]
        cl[i] -= i_calc * 1000000

pr = ''
for i in range(len(cl)):
    if i != 0:
        prt = str(cl[len(cl)-1-i]).zfill(6)
    else:
        prt = str(cl[len(cl)-1-i])
    pr += prt
print(pr)