def compute(n: int, dominos: list[int]) -> int:
    dp: list[tuple[int]] = [(1, dominos[i]) for i in range(n)]
    for i in range(1, n):
        domino = dominos[i]
        for j in range(i):
            now_count, _now_mass = dp[i]
            prev_count, total_mass = dp[j]
            if total_mass >= domino:
                if now_count <= prev_count + 1:
                    dp[i] = (prev_count + 1, total_mass + domino)
    result = -1
    for each in dp:
        if each[0] > result:
            result = each[0]
    return result

if __name__ == '__main__':
    n = int(input())
    dominos = list(map(int, input().split()))
    print(compute(n, dominos))
