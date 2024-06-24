q = sorted([*map(int, input().split())])
s = int(input())

i = 0
while q:
    p = q.pop()
    i += 1
    if p == s:
        break

if i < 6:
    print('A+')
elif i < 16:
    print('A0')
elif i < 31:
    print('B+')
elif i < 36:
    print('B0')
elif i < 46:
    print('C+')
elif i < 49:
    print('C0')
else:
    print('F')
