from sys import stdin
input = stdin.readline

for _i in range(int(input())):
  a, b, c = map(int, input().split())
  if a == b:
    print(c)
  if b == c:
    print(a)
  if c == a:
    print(b)
