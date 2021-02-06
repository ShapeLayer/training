from sys import stdin
n = int(stdin.readline())

i = 0 # 3kg
j = 0 # 5kg
while True:
    if n % 5 == 0:
        j = n // 5
        print(i+j)
        break
    else:
        i += 1
        n -= 3
    if n < 0:
        print(-1)
        break