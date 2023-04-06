n, s = list(map(int, input().split(':'))), list(map(int, input().split(':')))
dt = [s[0]-n[0]+23, s[1]-n[1]+59, s[2]-n[2]+60]
dt[1] += dt[2] // 60
dt[2] %= 60
dt[0] += dt[1] // 60
dt[1] %= 60
dt[0] %= 24
print('%02d:%02d:%02d' % (dt[0], dt[1], dt[2]))
