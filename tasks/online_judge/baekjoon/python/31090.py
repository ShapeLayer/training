from sys import stdin
input = stdin.readline

for _i in range(int(input())):
    n = int(input())
    if (n + 1) % (n % 100) == 0:
        print('Good')
    else:
        print('Bye')
