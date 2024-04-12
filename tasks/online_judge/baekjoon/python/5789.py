from sys import stdin
input = stdin.readline

for _i in range(int(input())):
    gets = input().strip()
    i = len(gets) // 2
    if gets[i - 1] == gets[i]:
        print('Do-it')
    else:
        print('Do-it-Not')
