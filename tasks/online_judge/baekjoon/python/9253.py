def generate_fail_arr(s: str) -> list[int]:
    m = len(s)
    fail = [0 for _i in range(m)]
    prefix, i = 0, 1
    while i < m:
        if s[i] == s[prefix]:
            prefix += 1
            fail[i] = prefix
            i += 1
        else:
            if prefix != 0:
                prefix = fail[prefix - 1]
            else:
                fail[i] = 0
                i += 1
    return fail

def kmp(text: str, ptrn: str, fail: list[int] = None):
    n, m = len(text), len(ptrn)
    if not fail:
        fail = generate_fail_arr(ptrn)
    i, j = 0, 0
    founds: list[int] = []
    while i < n:
        if text[i] == ptrn[j]:
            i += 1
            j += 1
        if j == m:
            return True
        elif i < n and text[i] != ptrn[j]:
            if j != 0:
                j = fail[j - 1]
            else:
                i += 1
    return False

if __name__ == '__main__':
    a, b, ptrn = input(), input(), input()
    fail = generate_fail_arr(ptrn)
    print('YES' if kmp(a, ptrn, fail) and kmp(b, ptrn, fail) else 'NO')
