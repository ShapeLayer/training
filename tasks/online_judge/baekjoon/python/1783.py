from sys import stdin
input = stdin.readline

def _move_lt_4(N, M, y, x, depth):
    new_depth = depth
    for dy, dx in ((-2, 1), (-1, 2), (1, 2), (2, 1)):
        ny, nx = y + dy, x + dx
        if not (0 <= ny < N and 0 <= nx < M):
            continue
        
        if depth < 3:
            new_depth = _move_lt_4(N, M, ny, nx, depth + 1)
    
    return new_depth


def compute(N: int, M: int):
    result = _move_lt_4(N, M, 0, 0, 0) + 1
    if N >= 3:
        result = max(result, M - 2)

    return result

if __name__ == "__main__":
    N, M = map(int, input().split())
    print(compute(N, M))
