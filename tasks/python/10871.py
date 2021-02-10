from sys import stdin

n, x = list(map(int, stdin.readline().split()))
nums = list(map(int, stdin.readline().split()))
corr = []
for num in nums:
    if num < x:
        corr += [num]
print(' '.join(map(str, corr)))