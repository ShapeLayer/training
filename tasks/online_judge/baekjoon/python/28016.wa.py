# WA

from sys import stdin
input = stdin.readline

def compute(n: int, m: int, ball: tuple[int], plate: list[list[int]]) -> int:
    availables = [0 for _i in range(m)]
    queue: list[tuple[int]] = [ball]

    def collide_handler(y: int, x: int) -> list[tuple[int]]:
        availables = []
        for dx in (1, -1):
            is_possible = True
            for dy in (0, 1):
                ny, nx = y + dy, x + dx
                if not (0 <= ny < n and 0 <= nx < m):
                    is_possible = False
                elif plate[ny][nx] == 1:
                    is_possible = False
                # print(f'({y}, {x}): dy, dx = {dy}, {dx} => {ny}, {nx} : {is_possible}({plate[ny][nx]})')
            if is_possible:
                availables.append(nx)
        return [(y + 1, able) for able in availables]

    def summary_result(availables: list[int]) -> int:
        max_idx, max_val = -1, -1
        is_all_zero = True
        for i in range(m):
            if availables[i] != 0:
                is_all_zero = False
            if availables[i] > max_val:
                max_val = availables[i]
                max_idx = i
        return max_idx if not is_all_zero else -1

    while queue:
        y, x = queue.pop()
        ny, nx = y + 1, x
        if not 0 <= ny < n:
            continue
        if plate[ny][nx] == 0:
            if ny == n - 1:
                availables[nx] += 1
            else:
                queue.append((ny, nx))
        else:
            for able in collide_handler(y, x):
                # print(f'queued: {able}')
                queue.append(able)
    
    return summary_result(availables)

if __name__ == '__main__':
    n, m = map(int, input().split())
    plate: list[list[int]] = []
    ball: tuple[int] = (0, 0)
    for i in range(n):
        row: list[int] = []
        gets: list[str] = input().split()
        for j in range(m):
            k = int(gets[j])
            if k == 2:
                ball = (i, j)
            row.append(k)
        plate.append(row)
    print(compute(n, m, ball, plate))
