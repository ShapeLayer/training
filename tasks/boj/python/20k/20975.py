# Edit Required
n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())), reverse=True)
cnt = 0
for each_a in a:
    flag = True
    for i in range(len(b)):
        if each_a > b[i]:
            flag = False
            break
    if not flag:
        cnt += 1
print(cnt)
