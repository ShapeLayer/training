from sys import stdin
input = stdin.readline

for _t in range(int(input())):
    a = [*sorted(map(int, input().split()))]
    print('YES' if a == [*sorted(map(int, input().split()))] and a[2] ** 2 == a[0] ** 2 + a[1] ** 2 else 'NO')
