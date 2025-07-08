from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    res = sum([*map(int, input().split())])
    if res > 0:
        print("Right")
    elif res < 0:
        print("Left")
    else:
        print("Equilibrium")
