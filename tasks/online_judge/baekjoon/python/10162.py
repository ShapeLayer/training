t = int(input())
if t % 10 != 0:
    print(-1)
else:
    fm = t//300
    m = (t-fm*300)//60
    ts = (t-(fm*300+m*60))//10
    print(fm, m, ts)