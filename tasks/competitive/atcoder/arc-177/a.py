from sys import stdin
input = stdin.readline

cost = [500, 100, 50, 10, 5, 1]
gets = [*map(int, input().split())][::-1]
n = int(input())
x = [*map(int, input().split())]
for each in x:
    for i in range(6):
        if each // cost[i] > 0:
            pay = min(each // cost[i], gets[i])
            each -= pay * cost[i]
            gets[i] -= pay
    if each > 0:
        print('No')
        exit()
print('Yes')
