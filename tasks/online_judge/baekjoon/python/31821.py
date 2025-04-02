from sys import stdin
input = stdin.readline

n = int(input())
menu = [int(input()) for _ in range(n)]
m = int(input())
print(sum([menu[int(input()) - 1] for _ in range(m)]))
