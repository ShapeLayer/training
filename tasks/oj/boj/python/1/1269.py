if __name__ == '__main__':
    dic = {}
    na, nb = map(int, input().split())
    count = na
    for i in map(int, input().split()):
        dic[i] = True
    for i in map(int, input().split()):
        if i not in dic:
            dic[i] = True
            count += 1
        else:
            dic[i] = False
            count -= 1
    print(count)
