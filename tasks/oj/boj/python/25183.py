n = int(input())
gets = [ord(s) for s in input()]
cnt = 1
flag = False
for i in range(1, n):
    if abs(gets[i] - gets[i-1]) == 1:
        cnt += 1
    else:
        cnt = 1
    if cnt >= 5:
        flag = True
print('YES' if flag else 'NO')
