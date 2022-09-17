for _i in range(int(input())):
    gets = bin(int(input()))[2:][::-1]
    ones = []
    for i in range(len(gets)):
        if gets[i] == '1': ones += [i]
    print(' '.join(map(str, ones)))
