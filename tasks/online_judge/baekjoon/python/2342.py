COST_TABLE = [ # [from][to]
    [1, 2, 2, 2, 2],
    [3, 1, 3, 4, 3],
    [3, 3, 1, 3, 4],
    [3, 4, 3, 1, 3],
    [3, 3, 4, 3, 1]
]

def compute(n: int, opers: list[int]) -> int:
    dp: list[tuple[tuple[int]]] = [((0, 0, 0), (0, 0, 0)) for _i in range(n + 1)]
    for i in range(n):
        oper = opers[i]
        pl, pr = dp[i]
        ll = COST_TABLE[pl[1]][oper]
        lr = COST_TABLE[pl[2]][oper]
        rl = COST_TABLE[pr[1]][oper]
        rr = COST_TABLE[pr[2]][oper]
        l, r = (0, 0, 0), (0, 0, 0)
        if pl[0] + ll < pr[0] + rl:
            l = (pl[0] + ll, oper, pl[2])
        else:
            l = (pr[0] + rl, oper, pr[2])
        if pl[0] + lr < pr[0] + rr:
            r = (pl[0] + lr, pl[1], oper)
        else:
            r = (pr[0] + rr, pr[1], oper)
        dp[i + 1] = (l, r)
    l, r = dp[-1]
    lc, rc = l[0], r[0]
    from json import dumps
    print(dumps(dp, indent=2))
    return lc if lc < rc else rc

if __name__ == '__main__':
    opers = list(map(int, input().split()))
    print(compute(len(opers) - 1, opers[:-1]))
