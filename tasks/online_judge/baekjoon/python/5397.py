from sys import stdin
input = stdin.readline

for _i in range(int(input())):
    gets = input().strip()
    p = 0
    puts = []
    for each in gets:
        if each == '<':
            p = max(0, p - 1)
        elif each == '>':
            p = min(len(puts) - 1, p + 1)
        elif each == '-':
            if puts:
                puts.pop(p)
                p -= 1
        else:
            puts.insert(p, each)
            p += 1
    print(''.join(puts))
