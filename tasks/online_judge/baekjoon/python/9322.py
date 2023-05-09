from sys import stdin
input = stdin.readline

for _t in range(int(input())):
    n = int(input())
    pub1, pub2, plain = [input().split() for _i in range(3)]

    result = [pub2.index(pub1[i])for i in range(n)]
    print(' '.join([plain[i] for i in result]))
