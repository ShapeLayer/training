from sys import stdin
input = stdin.readline

m = int(input())
s = [each == '1' for each in input().strip()]

prev = False
changes = []
i = 0
while i < m:
    if prev != s[i]:
        for j in range(i, m):
            if s[i] != s[j]:
                changes.append((i, j - 1, prev))
                i = -(j)
                prev = not prev
                break
            if j == m - 1:
                changes.append((i, j, prev))
                i = -(j + 1)
    if i < 0:
        i = -i
    else:
        i += 1
a = True
buf = []
for each in changes[::-1]:
    if not each[2]:
        buf.append('A' * (each[1] + 1))
        buf.append('B' * (each[0]))
    else:
        continue
    a = not a

s = ''.join(buf)
print(len(s))
print(s)
