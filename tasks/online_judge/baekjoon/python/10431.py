from sys import stdin
import heapq
input = stdin.readline

for _i in range(int(input())):
    gets = [*map(int, input().split())]
    n = gets[0]
    hq = []
    for each in gets[1:]:
        
