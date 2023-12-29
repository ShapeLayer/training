from sys import stdin
input = stdin.readline

for _i in range(int(input())):
  n = int(input())
  gets = [[*map(int, input().split())] for _i in range(n)]
  gets.sort(key=lambda each: (each[1] - each[0], each[0], each[1]), reverse=True)
  count = 0
  for i in range(n):
    now = gets[i]
    for j in range(i + 1, n):
      target = gets[j]
      if now[0] <= target[0] and target[1] <= now[1]:
        count += 1
  print(count)
