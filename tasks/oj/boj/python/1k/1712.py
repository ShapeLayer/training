from sys import stdin
cost = list(map(int, stdin.readline().split()))

if (cost[2] - cost[1]) == 0:
    result = -1
else:
    result = cost[0] // (cost[2] - cost[1]) + 1
    
if result < 0:
    result = -1
print(result)