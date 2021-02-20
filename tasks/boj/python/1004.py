from sys import stdin
t = int(stdin.readline())

def check_circle_range(cx, cy, cr, tx, ty):
    if (cx-tx)**2+(cy-ty)**2 < cr**2:
        return True
    return False

for _ in range(t):
    x1, y1, x2, y2 = list(map(int, stdin.readline().split()))
    n = int(stdin.readline())
    p_sys_arr = []
    thru = 0
    for i in range(n):
        p_sys_arr += [list(map(int, stdin.readline().split()))]
    for p_sys in p_sys_arr:
        cnt = 0
        if check_circle_range(p_sys[0], p_sys[1], p_sys[2], x1, y1):
            cnt += 1
        if check_circle_range(p_sys[0], p_sys[1], p_sys[2], x2, y2):
            cnt += 1
        if cnt % 2 == 1:
            thru += 1
    print(thru)