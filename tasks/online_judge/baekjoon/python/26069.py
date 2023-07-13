from sys import stdin
from collections import defaultdict
input = stdin.readline

def compute(n: int, gets: list[str]) -> int:
    dances: int = 1
    is_dance: defaultdict = defaultdict(bool)
    is_dance['ChongChong'] = True
    for a, b in gets:
        if is_dance[a] and not is_dance[b]:
            is_dance[b] = True
            dances += 1
        elif is_dance[b] and not is_dance[a]:
            is_dance[a] = True
            dances += 1
    return dances

if __name__ == '__main__':
    n = int(input())
    gets: list[str] = [input().split() for _i in range(n)]
    print(compute(n, gets))
