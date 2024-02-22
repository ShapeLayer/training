from sys import stdin
input = stdin.readline

n, t = input().split()
n = int(n)
g = 1 if t == 'Y' else 2 if t == 'F' else 3
print(len(set([input().strip() for _i in range(n)])) // g)
