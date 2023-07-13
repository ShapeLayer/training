from sys import stdin
from collections import defaultdict
input = stdin.readline

def compute(n: int, m: int, gets: list[str]) -> list[str]:
    counts: defaultdict = defaultdict(int)
    lengths: dict = {}
    for each in gets:
        counts[each] += 1
        if each not in lengths:
            lengths[each] = len(each)
    result = sorted(dict(counts).keys(), key=lambda each: (-counts[each], -len(each), each))
    return result

if __name__ == '__main__':
    n, m = map(int, input().split())
    targets: list[str] = []
    for i in range(n):
        gets: str = input().strip()
        if len(gets) >= m:
            targets.append(gets)
    print('\n'.join(compute(n, m, targets)))
