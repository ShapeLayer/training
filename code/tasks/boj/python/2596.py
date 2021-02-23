len_ = int(input())
text = input()
tsplit = []
define = {
    'A': list('000000'),
    'B': list('001111'),
    'C': list('010011'),
    'D': list('011100'),
    'E': list('100110'),
    'F': list('101001'),
    'G': list('110101'),
    'H': list('111010')
}
res = ''

for i in range(len_):
    tsplit += [text[i*6:i*6+6]]
for j in range(len(tsplit)):
    cnt = [6 for _ in range(8)]
    for i in range(6):
        if tsplit[j][i] == define['A'][i]:
            cnt[0] -= 1
        if tsplit[j][i] == define['B'][i]:
            cnt[1] -= 1
        if tsplit[j][i] == define['C'][i]:
            cnt[2] -= 1
        if tsplit[j][i] == define['D'][i]:
            cnt[3] -= 1
        if tsplit[j][i] == define['E'][i]:
            cnt[4] -= 1
        if tsplit[j][i] == define['F'][i]:
            cnt[5] -= 1
        if tsplit[j][i] == define['G'][i]:
            cnt[6] -= 1
        if tsplit[j][i] == define['H'][i]:
            cnt[7] -= 1
    if (0 in cnt or 1 in cnt) and (j == 0 or res not in '2345678910'):
        if 0 in cnt:
            res += chr(cnt.index(0)+65)
        else:
            res += chr(cnt.index(1)+65)
    elif res in '2345678910':
        pass
    else:
        res = str(j+1)
print(res)