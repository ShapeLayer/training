from sys import stdin
x, y, w, h = list(map(int, stdin.readline().split()))
d = [x-0, y-0, w-x, h-y]
print(min(d))