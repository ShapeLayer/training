from sys import stdin
gets = stdin.readline
for _i in range(int(gets())):
    cloths = {}
    n = int(gets())
    for _j in range(n):
        type_ = gets().split()[1]
        if type_ not in cloths:
            cloths[type_] = 1
        else:
            cloths[type_] += 1
    res = 1
    for n in cloths.values():
        res *= n+1
    res -= 1
    print(res)