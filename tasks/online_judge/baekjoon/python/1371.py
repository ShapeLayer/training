from sys import stdin
input = stdin.readline

def compute(content: str) -> list[str]:
    counts = [0 for _i in range(26)]
    for char in content:
        c = ord(char)
        if 97 <= c <= 122:
            counts[c - 97] += 1
    mx: int = max(counts)
    result: list[str] = []
    for i in range(26):
        if counts[i] == mx:
            result.append(chr(i + 97))
    return result

if __name__ == '__main__':
    gets: str = ''
    strings: list[str] = []
    while True:
        try:
            gets = input().strip()
        except EOFError:
            break
        if gets == '':
            break
        strings.append(gets)
    string: str = ''.join(strings)
    print(*compute(string))
