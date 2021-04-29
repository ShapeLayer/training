from sys import stdin
r = [0, 0]

c = 0
while True:
    c += 1
    try:
        t = int(stdin.readline())
    except:
        break
    if r[0] < t:
        r[0] = t
        r[1] = c
print(r[0])
print(r[1])