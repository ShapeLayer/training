from sys import stdin
from collections import defaultdict
input = stdin.readline

def compute(n: int, gets: list):
    rings = defaultdict(list)
    for name, ring in gets:
        if ring == '-':
            continue
        rings[ring].append(name)
    couples = []
    for ring in rings:
        if len(rings[ring]) == 2:
            couples.append(rings[ring])
    return couples

if __name__ == '__main__':
    n = int(input())
    gets = [input().split() for _i in range(n)]
    res = compute(n, gets)
    print(len(res))
    for each_couple in res:
        print(*each_couple)
