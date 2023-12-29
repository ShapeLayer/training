from sys import stdin
input = stdin.readline

for _i in range(int(input())):
  n = int(input())
  gets = sum(map(int, input().split()))
  if int(gets ** .5) ** 2 == gets:
    print('YES')
  else:
    print('NO')

