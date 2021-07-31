# Timeout
n = int(input())
cnt = 0
for i in range(1, n+1):
    divs = []
    for j in range(1, int(i**0.5)+1):
        if i % j == 0:
            divs += [j]
            divs += [i//j]
    cnt += 1 if len(set(divs)) % 2 == 1 else 0
print(cnt)
