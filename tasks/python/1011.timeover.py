from sys import stdin
t = int(stdin.readline())
for a in range(t):
    d1, d2 = list(map(int, stdin.readline().split()))
    n = d2 - d1
    dis_li = [2]
    loop = True
    while loop:
        dis = 0
        for i in range(len(dis_li)):
            dis += dis_li[i] * (i+1)
        if dis == n:
            loop = False
        else:
            if 3 in dis_li:
                if dis_li.index(3) == len(dis_li) - 1:
                    dis_li += [1]
                else:
                    dis_li[dis_li.index(3) + 1 ] += 1
                dis_li[dis_li.index(3)] -= 1
            else:
                dis_li[0] += 1
        print(dis_li)

    print(sum(dis_li))