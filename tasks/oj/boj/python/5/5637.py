gets = ''
while True:
    gets += input()
    if gets[-5:] == 'E-N-D':
        break
maxs = ''
res = ''
for s in gets.lower():
    if s in 'abcdefghijklmnopqrstuvwxyz-':
        res += s
    else:
        if len(maxs) < len(res):
            maxs = res
        res = ''
print(maxs)