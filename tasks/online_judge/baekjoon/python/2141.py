from sys import stdin
input = stdin.readline

def compute(n: int, gets: list[list[int]]):
    limit = sum([each[1] for each in gets]) / 2
    _sum = 0
    ptr = -1
    for x, a in gets:
        ptr = x
        _sum += a
        if limit <= _sum:
            return x
    return ptr

if __name__ == '__main__':
    n = int(input())
    gets = sorted([[*map(int, input().split())] for _i in range(n)])
    print(compute(n, gets))
