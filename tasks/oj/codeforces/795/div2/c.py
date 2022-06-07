# Wrong answer on pretest 2

# 11111110
# 11111101
# 01010101 => 10101010 (10+1+10+1+10+1+10)
# 0 개수: 4, 1 개수: 4 (합연산 7개)
# 01010101 => 1 + 10 + 1 + 10 + 1 + 10 + 1
# 01010110 => 1 + 10 + 1 + 10 + 1 + 11 + 10
# 101010100

from sys import stdin
input = stdin.readline
for _t in range(int(input())):
    n, k = map(int, input().split())
    string = list(input().rstrip())
    zeros = []
    length = len(string)
    done = [-1, length]
    if string[-1] == '0': zeros.append(length-1)
    idx = [0, length - 1]
    zeros = [[], []]
    while idx[0] < idx[1]:
        if string[idx[0]] == '0': zeros[0] += [idx[0]]
        if string[idx[1]] == '0': zeros[1] += [idx[1]]
        for i in range(2):
            if string[idx[i]] == '1':
                if not zeros[i]: continue
                if length % 2 == 1 and idx[i] == length // 2:
                    if done[0] > length - done[1] and i == '1': continue
                    if done[0] < length - done[1] and i == '0': continue
                zero = zeros[i][0]
                if zero - idx[i] <= k and zero > idx[i]:
                    zeros[i].pop(0)
                    string[idx[i]], string[zero] = string[zero], string[idx[i]]
                    zeros[i].append(idx[i])
                    done[i] = zero
                    k -= abs(zero - idx[i])
        idx[0] += 1
        idx[1] -= 1
    sums = 0
    for i in range(1, length):
        sums += int(''.join(string[i-1:i+1]))
    print(sums)