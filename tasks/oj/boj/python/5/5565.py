from sys import stdin
s = int(stdin.readline())
for _ in range(9):
    s -= int(stdin.readline())
print(s)