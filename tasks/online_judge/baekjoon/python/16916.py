def compute(s: str, p: str) -> bool:
    ln_s, ln_p = len(s), len(p)
    for i in range(ln_s - ln_p + 1):
        is_included = True
        for j in range(ln_p):
            if s[i + j] != p[j]:
                is_included = False
                break
        if is_included:
            return True
    return False

if __name__ == '__main__':
    s, p = input(), input()
    print(int(compute(s, p)))
