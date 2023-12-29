from sys import stdin
input = stdin.readline

for _i in range(int(input())):
  for _j in range(3):
    gets = input().strip()
    if 'A' in gets and 'B' in gets and 'C' in gets:
      pass
    elif 'A' not in gets:
      print('A')
    elif 'B' not in gets:
      print('B')
    elif 'C' not in gets:
      print('C')
