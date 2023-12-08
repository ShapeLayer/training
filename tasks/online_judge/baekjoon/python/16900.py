def gen_fail_arr(s: str) -> list[int]:
    n = len(s)
    fail = [0 for _i in range(n)]
    pre, post = 0, 1
    while post < n:
        if s[pre] == s[post]:
            pre += 1
            fail[post] = pre
            post += 1
        else:
            if pre != 0:
                pre = fail[pre - 1]
            else:
                fail[post] = 0
                post += 1
    return fail

def compute(s: str, k: int):
    n = len(s)
    fail = gen_fail_arr(s)
    return n * k - (fail[n - 1] * (k - 1))

if __name__ == '__main__':
    s, k = input().split()
    k = int(k)
    print(compute(s, k))
