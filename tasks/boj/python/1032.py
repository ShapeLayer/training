from sys import stdin

n = int(stdin.readline())
arr = []
for _ in range(n):
    arr += [stdin.readline()]

result = ''
for i in range(len(arr[0])):
    now = ''
    for j in range(len(arr)):
        if j != 0:
            if now != '':
                if arr[j][i] != now:
                    now = ''
        else:
            now = arr[j][i]
    if now:
        result += now
    else:
        result += '?'
print(result)