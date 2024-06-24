n = int(input())
gets = [[*map(int, input().split())] for _i in range(n)]
s, e = gets[0]
for _s, _e in gets[1:]:
    s, e = max(s, _s), min(e, _e)
if s > e:
    print('edward is right')
else:
    print('gunilla has a point')
