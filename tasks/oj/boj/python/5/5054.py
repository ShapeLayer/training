for _i in range(int(input())):
    n = int(input())
    gets = list(map(int, input().split()))
    e = sum(gets)//n
    sums = 2 * (max(gets) - min(gets))
    print(sums)
