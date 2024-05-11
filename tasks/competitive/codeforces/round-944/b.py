from sys import stdin
from collections import Counter
input = stdin.readline

for _i in range(int(input())):
    gets = list(input().strip())
    s = set(list(gets))
    if len(s) == 1:
        print('NO')
    else:
        for i in range(1, len(gets)):
            if gets[i - 1] != gets[i]:
                gets[i - 1], gets[i] = gets[i], gets[i - 1]
                break
        print('YES')
        print(''.join(gets))
