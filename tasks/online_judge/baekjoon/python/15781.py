from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
print(max(*map(int, input().split())) + max(*map(int, input().split())))
