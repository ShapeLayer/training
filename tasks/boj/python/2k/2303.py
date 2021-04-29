from sys import stdin

def get_max(arr):
    s = []
    for a in range(3):
        for b in range(3-a):
            for c in range(3-a-b):
                s += [(arr[a]+arr[a+b+1]+arr[a+b+c+2])%10]
    return max(s)

arr = []
his = {}
for i in range(int(stdin.readline())):
    arr += [list(map(int, stdin.readline().split()))]
np = True
for i in range(len(arr)-1, -1, -1):
    m = get_max(arr[i])
    if m == 9:
        print(i+1)
        np = False
        break
    elif m not in his:
        his[m] = i+1
if np:
    print(his[max(his.keys())])