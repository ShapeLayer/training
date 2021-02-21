n = int(input())
i = 2
while n != 1:
    calc = n / i
    if calc == n // i:
        print(i)
        n = calc
    else:
        i += 1