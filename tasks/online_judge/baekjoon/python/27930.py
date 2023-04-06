s = input()
cnt_korea, cnt_yonsei = 0, 0
for c in s:
    if c == 'KOREA'[cnt_korea]:
        cnt_korea += 1
    if c == 'YONSEI'[cnt_yonsei]:
        cnt_yonsei += 1

    if cnt_korea == 5:
        print('KOREA')
        break
    elif cnt_yonsei == 6:
        print('YONSEI')
        break
