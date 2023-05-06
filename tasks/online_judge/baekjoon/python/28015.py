from sys import stdin
input = stdin.readline

def compute(canvas: list[int]) -> int:
    coloring: int = 0
    for line in canvas:
        prev: int = 0
        change_to: list[int] = [1e10, 0, 0] # [0, 1, 2]
        change_to_updated = True
        for dot in line:
            if prev != dot:
                if dot != 0:
                    change_to[dot] += 1
                    change_to_updated = False
                else:
                    coloring += min(change_to) + 1
                    change_to = [1e10, 0, 0]
                    change_to_updated = True
            prev = dot
        if not change_to_updated:
            coloring += min(change_to) + 1
    return coloring

if __name__ == '__main__':
    n, m = map(int, input().split())
    canvas = [list(map(int, input().split())) for _i in range(n)]
    print(compute(canvas))
