from sys import stdin
input = stdin.readline

for _i in range(int(input())):
  input()
  gets = input().strip()
  buf = []
  n = len(gets)
  p = 0

  cache = []
  while p < n:
    if gets[p] in 'bcd':
      cache.append(gets[p])
    else:
      if p < n - 2 and gets[p + 1] in 'bcd' and gets[p + 2] in 'bcd':
        cache.append(gets[p])
        cache.append(gets[p + 1])
        p += 1
      elif p == n - 2 and gets[p + 1] in 'bcd':
        cache.append(gets[p])
        cache.append(gets[p + 1])
        p += 1
      else:
        cache.append(gets[p])
      buf.append(''.join(cache))
      cache = []
    p += 1
  print('.'.join(buf))
