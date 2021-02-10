from sys import stdin
n = int(stdin.readline())

finder = 0
i = 0
while True:
    if i == 0:
        finder += 1
    else:
        finder += 6*i
    if finder >= n:
        break
    i += 1

print(i+1)