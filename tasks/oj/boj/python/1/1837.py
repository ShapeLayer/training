from time import time
p, k = map(int, input().split())
pl = [False if i < 2 else True for i in range(k)]
p_arr = []
for i in range(len(pl)):
    if pl[i]:
        p_arr += [i]
        for j in range(2*i, len(pl), i):
            pl[j] = False
is_up = True
for pn in p_arr:
    if p%pn == 0:
        print('BAD', pn)
        is_up = False
        break
if is_up:
    print('GOOD')