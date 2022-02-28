n = int(input())
puts = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))
numdict = {i: 0 for i in map(int, nums)}
for put in puts:
    if put in numdict:
        numdict[put] = 1
res = '\n'.join([str(numdict[i]) for i in nums])
print(res)