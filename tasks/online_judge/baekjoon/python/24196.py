def compute(gets: str) -> str:
    buf = []
    a = ord('A')
    n, p = len(gets), 0
    while p < n:
        buf.append(gets[p])
        p += ord(gets[p]) - a + 1
    return ''.join(buf)

if __name__ == '__main__':
    gets = input()
    print(compute(gets))
