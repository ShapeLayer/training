_, s = input(), input()
stacked = 0
prev = None
flag = False
for each in s:
    if each == 'o':
        if prev == each:
            stacked += 1
        else:
            stacked = 1
        if stacked >= 3:
            flag = True
    else:
        stacked = 0
    prev = each
print('Yes' if flag else 'No')
