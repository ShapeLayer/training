from math import ceil
from sys import stdin
input = stdin.readline

def compute(n: int, l: int, gets: list[list[int]]) -> int:
    gets.sort()
    end = -1
    counts = 0
    for s, e in gets:
        if s > end:
            req = ceil((e - s) / l)
            counts += req
            end = s + req * l
        elif e > end:
            req = ceil((e - end) / l)
            counts += req
            end += req * l
    return counts

if __name__ == '__main__':
    n, l = map(int, input().split())
    gets = [[*map(int, input().split())] for _i in range(n)]
    print(compute(n, l, gets))
