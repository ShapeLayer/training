for _i in range(int(input())):
    dic = {}
    for _j in range(int(input())):
        a, b = input().split()
        a = int(a)
        dic[a] = b
    print(dic[max(dic.keys())])
