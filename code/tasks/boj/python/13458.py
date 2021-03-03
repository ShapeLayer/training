from math import ceil
n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

manager = 0
for a in arr:
    leave = a - b
    manager += 1
    if leave > 0:
        manager += ceil(leave/c)
print(manager)