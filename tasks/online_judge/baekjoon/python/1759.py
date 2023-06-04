def compute(l: int, c: int, chars: list[str]) -> list[str]:
    chars.sort()
    buf = []
    def ptr_pick_runner(i: int, ln: int, selected: list[int]):
        if ln == l:
            able_buf: list[str] = []
            vow, con = 0, 0
            for i in selected:
                char = chars[i]
                if char in 'aeiou':
                    vow += 1
                else:
                    con += 1
                able_buf.append(char)
            if vow >= 1 and con >= 2:
                buf.append(''.join(able_buf))
            return
        for j in range(i + 1, c):
            ptr_pick_runner(j, ln + 1, selected + [j])
    ptr_pick_runner(-1, 0, [])
    return buf

if __name__ == '__main__':
    l, c = map(int, input().split())
    chars: list[str] = input().split()
    result: list[str] = compute(l, c, chars)
    print('\n'.join(result))
