from sys import stdin
input = stdin.readline

for _i in range(int(input())):
    gets = input().strip()
    if gets == 'P=NP':
        print('skipped')
    else:
        a, b = map(int, gets.split('+'))
        print(a + b)
