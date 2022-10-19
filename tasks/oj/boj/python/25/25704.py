n, p = int(input()), int(input())
stampidx = n // 5
prices = []
for i in range(min(5, stampidx+1)):
    if i == 0: prices += [p]
    elif i == 1: prices += [max(0, p - 500)]
    elif i == 2: prices += [p * 0.9]
    elif i == 3: prices += [max(0, p - 2000)]
    elif i == 4: prices += [p * 0.75]
print(int(min(prices)))