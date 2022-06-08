gets = [int(input()) for _i in range(7)]
odds = []
for get in gets:
    if get % 2 == 1: odds += [get]

if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)
