from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
result = 1
for each in map(lambda each: each % m, map(int, input().split())):
    result = (result * each) % m
print(result)
