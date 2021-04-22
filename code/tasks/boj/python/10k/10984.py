from sys import stdin
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s_c, s_g, gps = [], [], 0
    for i in range(n):
        c, g = map(float, stdin.readline().split())
        s_c += [c]
        s_g += [g]
    for i in range(n):
        gps += s_c[i]*s_g[i]
    print(int(sum(s_c)), format(gps/sum(s_c), '.1f'))