from sys import stdin
input = stdin.readline

while True:
    n = input().strip()
    if n == '0':
        break
    while len(n) > 1:
        res = 0
        for char in n:
            res += int(char)
        n = str(res)
    print(n)
