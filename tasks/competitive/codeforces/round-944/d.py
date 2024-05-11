from sys import stdin
input = stdin.readline

for _i in range(int(input())):
    gets = input().strip()
    _1to0, _0to1 = 0, 0
    for i in range(1, len(gets)):
        _1to0 += int(gets[i - 1] == '1' and gets[i] == '0')
        _0to1 += int(gets[i - 1] == '0' and gets[i] == '1')
    print(_0to1, _1to0)
    print(_1to0 + max(_0to1 - 1, 0) + 1)
