from sys import stdin

dic = {}
val = 0

for _ in range(int(stdin.readline())):
    puts = stdin.readline().split()
    p, key = puts[0], puts[1]
    if p == '1':
        arr = list(map(int, puts[3:]))
        if key in dic.keys():
            dic[key] = sorted(dic[key] + arr)
        else:
            dic[key] = sorted(arr)
    else:
        if key in dic.keys():
            if int(puts[2]) <= len(dic[key]):
                for __ in range(int(puts[2])):
                    val += dic[key].pop()
            else:
                val += sum(dic[key])
                dic[key] = []
print(val)
