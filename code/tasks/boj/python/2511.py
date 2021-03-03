a = list(map(int, input().split()))
b = list(map(int, input().split()))
history, pnt = [], [0, 0]
for i in range(10):
    if a[i] > b[i]:
        history += ['A']
        pnt[0] += 3
    elif a[i] < b[i]:
        history += ['B']
        pnt[1] += 3
    else:
        history += ['D']
        pnt[0] += 1
        pnt[1] += 1
print(pnt[0], pnt[1])
if pnt[0] > pnt[1]:
    print('A')
elif pnt[1] < pnt[0]:
    print('B')
else:
    np = True
    for i in range(9, 0, -1):
        if history[i] != 'D':
            np = False
            print(history[i])
            break
    if np:
        print('D')