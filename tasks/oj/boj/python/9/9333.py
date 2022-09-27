dic = {}
for _i in range(int(input())):
    gets = input()
    dic[gets] = True
    if gets[::-1] in dic:
        print(len(gets), gets[len(gets)//2])