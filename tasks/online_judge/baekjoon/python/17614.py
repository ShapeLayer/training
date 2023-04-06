cnt = 0
for i in range(int(input())+1):
    n = i
    while n:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9: cnt += 1
        n //= 10
print(cnt)
