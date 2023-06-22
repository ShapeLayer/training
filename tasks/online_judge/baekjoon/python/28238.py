from sys import stdin
input = stdin.readline

def compute(n: int, applies: list[tuple[bool]]):
    lec_day = [0, 1]
    max_ables = 0
    for i in range(4):
        for j in range(i + 1, 5):
            now_ables = 0
            for apply in applies:
                if apply[i] and apply[j]:
                    now_ables += 1
            if now_ables > max_ables:
                lec_day = [i, j]
                max_ables = now_ables
    result = [0, 0, 0, 0, 0]
    result[lec_day[0]] = 1
    result[lec_day[1]] = 1
    return max_ables, result

if __name__ == '__main__':
    n = int(input())
    applies: list[tuple[bool]] = [tuple(map(bool, map(int, input().split()))) for _i in range(n)]
    max_ables, result = compute(n, applies)
    print(max_ables)
    print(*result)
