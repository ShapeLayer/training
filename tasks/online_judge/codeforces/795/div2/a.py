from sys import stdin
input = stdin.readline

for _i in range(int(input())):
    input()
    odd, even = 0, 0
    for n in map(int, input().split()):
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    print(min(odd, even))