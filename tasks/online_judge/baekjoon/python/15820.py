from sys import stdin
input = stdin.readline

def compute(s1: int, s2: int, sample: list[tuple[int]], system: list[tuple[int]]) -> int:
    for case in sample:
        ans, sub = case
        if ans != sub:
            return 1
    for case in system:
        ans, sub = case
        if ans != sub:
            return 2
    return 0

if __name__ == '__main__':
    s1, s2 = map(int, input().split())
    sample: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(s1)]
    system: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(s2)]
    result = compute(s1, s2, sample, system)
    if result == 0:
        print('Accepted')
    elif result == 1:
        print('Wrong Answer')
    else:
        print('Why Wrong!!!')
