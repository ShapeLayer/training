from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    a, b = list(map(int, stdin.readline().split()))
    print(a**b%10)