from sys import stdin

t = stdin.readline()

cnt = 0
for i in range(len(t)):
    ti = t[i]
    if ti in ['A', 'B', 'C']:
        cnt += 3
    elif ti in ['D', 'E', 'F']:
        cnt += 4
    elif ti in ['G', 'H', 'I']:
        cnt += 5
    elif ti in ['J', 'K', 'L']:
        cnt += 6
    elif ti in ['M', 'N', 'O']:
        cnt += 7
    elif ti in ['P', 'Q', 'R', 'S']:
        cnt += 8
    elif ti in ['T', 'U', 'V']:
        cnt += 9
    elif ti in ['W', 'X', 'Y', 'Z']:
        cnt += 10
print(cnt)