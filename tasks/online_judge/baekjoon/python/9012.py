from sys import stdin

def chk_vps(string: str):
    cnt = 0
    flag = True
    for s in string:
        if s == '(':
            cnt += 1
        elif s == ')':
            cnt -= 1
        if cnt < 0:
            flag = False
    if cnt != 0:
        flag = False
    return flag

for _ in range(int(stdin.readline())):
    if chk_vps(stdin.readline()):
        print('YES')
    else:
        print('NO')
