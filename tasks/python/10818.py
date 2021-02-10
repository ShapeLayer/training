from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().strip().split()))
print(min(nums), max(nums))