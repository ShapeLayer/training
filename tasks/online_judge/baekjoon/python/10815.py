n = input()
gets = {i: True for i in map(int, input().split())}
m = input()
find = map(int, input().split())

arr = []
for each in find:
    if each in gets:
        arr.append('1')
    else:
        arr.append('0')

print(' '.join(arr))
