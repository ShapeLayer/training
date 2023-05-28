from sys import stdin
input = stdin.readline

def compute(n: int, m: int, relations: list[tuple[int]]) -> list[int]:
    rel_map = { i: 0 for i in range(1, n + 1) }
    for relation in relations:
        a, b = relation
        rel_map[a] += 1
        rel_map[b] += 1
    return rel_map.values()

if __name__ == '__main__':
    n, m = map(int, input().split())
    relations: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(m)]
    print('\n'.join(map(str, compute(n, m, relations))))
