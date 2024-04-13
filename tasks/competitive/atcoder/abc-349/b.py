from sys import stdin
from collections import Counter
input = stdin.readline

if __name__ == '__main__':
    s = dict(Counter(dict(Counter(input().strip())).values())).values()
    flag = False
    for each in s:
        if each != 0 and each != 2:
            flag = True
            break
    print('Yes' if not flag else 'No')
