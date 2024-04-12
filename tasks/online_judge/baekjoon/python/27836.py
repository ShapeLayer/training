from sys import stdin
input = stdin.readline

for _i in range(int(input())):
    input()
    n, m = map(int, input().split())
    c = [*map(int, input().split())]
    e = [*map(int, input().split())]
    c_sum, e_sum = sum(c), sum(e)
    
    print(sum([int(c_sum > c[j] * n and e_sum < c[j] * m) for j in range(n)]))
