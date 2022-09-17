from sys import stdin
from collections import Counter
input = stdin.readline

prices = []
for _i in range(int(input())):
    gets = dict(Counter(map(int, input().split())))
    if 4 in gets.values():
        prices += [50000 + gets.keys() * 5000]
    elif 3 in gets.values():
        for i in gets:
            if gets[i] == 3:
                prices += [10000 + i * 1000]
    elif {2} == set(gets.values()):
        sums = 2000
        sums += 
#todo0614