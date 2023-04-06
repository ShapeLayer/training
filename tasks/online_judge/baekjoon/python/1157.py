from sys import stdin

txt = stdin.readline().rstrip()
cnt = [0 for i in range(26)]

for i in range(len(txt)):
    tord = ord(txt[i])
    if tord > 96:
        tord -= 32
    cnt[tord-65] += 1

max_ = max(cnt)
if cnt.count(max_) == 1:
    print(chr(cnt.index(max_)+65))
else:
    print('?')