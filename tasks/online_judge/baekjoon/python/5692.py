from sys import stdin
input = stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    fact, i = 1, 1
    result = 0
    while n:
        result += (n % 10) * fact
        i += 1
        fact *= i
        n //= 10
    print(result)
