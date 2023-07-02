from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10000)

def eval_diff(_len: int, a: str, b: str) -> int:
    diff: int = 0
    for i in range(_len):
        if a[i] != b[i]:
            diff += 1
    return diff

def compute(n: int, m: int, k: int, tiles: list[str], appeared: list[str]) -> tuple:
    able_len: int = len(appeared)

    def bruteforce(order: int, select: int, curr: list[str]):
        total_diff: list[tuple] = []
        for i in range(able_len):
            if order == k * k - 1:
                done: str = curr + [appeared[select]]
                diff: int = evaluate(''.join(done))
                total_diff.append((diff, done))
            else:
                each_diff: list[tuple] = bruteforce(order + 1, i, curr + [appeared[select]])
                total_diff += each_diff
        return total_diff

    def evaluate(curr: str) -> int:
        total_diff: int = 0
        for i in range(n // k):
            for j in range(m // k):
                selected = ''.join([row[j * k:(j + 1) * k] for row in tiles[i * k:(i + 1) * k]])
                total_diff += eval_diff(k * k, curr, selected)
        return total_diff

    tries: list[tuple] = []
    for i in range(able_len):
        tries += bruteforce(0, i, [])

    tries.sort()
    result = tries[0][1]
    buf = []
    y_rept, x_rept = n // k, m // k
    for i in range(k):
        row = ''.join([''.join(result[i * k:(i + 1) * k]) for _j in range(x_rept)])
        buf.append(row)
    buf *= y_rept
    return tries[0][0], '\n'.join(buf)


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    tiles: list[str] = []
    appeared: set[str] = set()
    for _i in range(n):
        gets = input().strip()
        tiles.append(gets)
        appeared = appeared.union(set(gets))
    rn, res = compute(n, m, k, tiles, list(appeared))
    print(rn)
    print(res)
