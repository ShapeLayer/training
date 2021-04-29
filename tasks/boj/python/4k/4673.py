from sys import stdin

arr = [True for i in range(10001)]
for i in range(1, 10001):
    loop = True
    sums = []
    j = i
    while loop:
        calced = j % 10
        j = (j - calced) // 10
        sums += [calced]
        if j == 0:
            loop = False
    j = i + sum(sums)
    if j <= 10000:
        arr[j] = False
  
for i in range(1, 10001):
    if arr[i]:
        print(i)