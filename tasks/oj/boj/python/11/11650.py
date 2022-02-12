dic = {}
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x in dic:
        dic[x] += [y]
    else:
        dic[x] = [y]
for keys in dic:
    dic[keys].sort()
for key in sorted(dic.keys()):
    for val in dic[key]:
        print(key, val)