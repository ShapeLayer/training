from sys import stdin
input = stdin.readline

arr = [0, 0, 0, 0]

for _i in range(int(input())):
    a, b = input().split()
    b = int(b)
    if a == 'STRAWBERRY':
        arr[0] += b
    elif a == 'BANANA':
        arr[1] += b
    elif a == 'LIME':
        arr[2] += b
    else:
        arr[3] += b

print('YES' if 5 in arr else 'NO')
