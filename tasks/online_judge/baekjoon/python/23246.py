from sys import stdin
innput = stdin.readline

def compute(n: int, scores: list[tuple[int]]) -> list[int]:
    calcs: list[tuple[int]] = []
    for score in scores:
        back, a, b, c = score
        calcs.append((a * b * c, a + b + c, back))
    calcs.sort()
    return [each[2] for each in calcs[:3]]

if __name__ == '__main__':
    n = int(input())
    scores: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    print(*compute(n, scores))
