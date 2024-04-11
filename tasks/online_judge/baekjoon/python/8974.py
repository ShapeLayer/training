a, b = map(int, input().split())
flag, cnt, sum_ = 1, 1, 0
for i in range(1, b+1):
    if a <= i:
        sum_ += cnt
    if flag == cnt:
        cnt += 1
        flag = 0
    flag += 1
print(sum_)
