from sys import stdin
input = stdin.readline

table = {
    '@': 'a',
    '[': 'c',
    '!': 'i',
    ';': 'j',
    '^': 'n',
    '0': 'o',
    '7': 't',
    '\\\'': 'v',
    '\\\\\'': 'w'
}

def compute(gets: str) -> str:
    length: int = len(gets)
    counts: int = 0
    buf: list[str] = []
    offset: int = 0
    for i in range(length):
        if offset > 0:
            offset -= 1
            continue
        if gets[i] in table:
            buf.append(table[gets[i]])
            counts += 1
        elif gets[i] == '\\':
            hold = ['\\']
            if i + 1 < length and gets[i + 1] == '\'':
                buf.append('v')
                counts += 2
                offset += 1
                hold.clear()
            elif i + 1 < length and gets[i + 1] == '\\':
                hold.append('\\')
                offset += 1
                if i + 2 < length and gets[i + 2] == '\'':
                    buf.append('w')
                    counts += 3
                    offset += 1
                    hold.clear()
            buf += hold
            counts += len(hold)
        else:
            buf.append(gets[i])
    if length / 2 < counts:
        return None
    return ''.join(buf)

if __name__ == '__main__':
    n = int(input())
    for _i in range(n):
        result = compute(input().strip())
        print(result if result != None else 'I don\'t understand')
