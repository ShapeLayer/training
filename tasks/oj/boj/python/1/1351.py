dp = {0: 1}

def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)

def proc(n, nplcm, nqlcm):
    if n == 0: return dp[n]
    np = n // p
    nq = n // q
    for nn in (np, nq):
        if nn not in dp:
            proc(nn, nplcm, nqlcm)
    dp[n] = dp[np] + dp[nq]
    return dp[n]

if __name__ == '__main__':
    n, p, q = map(int, input().split())
    nplcm = n * p // gcd(n, p)
    nqlcm = n * q // gcd(n, q)
    print(proc(n, nplcm, nqlcm))