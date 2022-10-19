n = int(input())
panel = list(input())
m = int(input())
gets = input()
counts = 0
prev = None
for s in gets:
    if s not in panel:
        print(-1)
        exit()
    while panel[counts % n] != s:
        counts += 1
    counts += 1
print(counts)