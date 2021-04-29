from collections import Counter
cnt = Counter(list(map(int, input().split())))
if len(cnt) == 1:
    for i in cnt:
        r = 10000+i*1000
elif len(cnt) == 2:
    for i in cnt:
        if cnt[i] == 2:
            r = 1000+i*100
elif len(cnt) == 3:
    r = max(list(cnt))*100

print(r)