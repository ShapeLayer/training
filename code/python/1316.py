from sys import stdin

n = int(stdin.readline())

cnt = 0
for i in range(n):
    t = stdin.readline().rstrip()
    history = []
    prev = 0
    group = True
    for i in range(len(t)):
        ot = ord(t[i])
        if ot not in history:
            prev = ot
            history += [ot]
        elif prev != ot: # 직전에 연속된 문자가 없음
            group = False
    if group:
        cnt += 1
print(cnt)