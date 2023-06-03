from sys import stdin
input = stdin.readline

def compute(gets: str) -> str:
    result = [0 for _i in range(26)]
    for char in gets:
        o = ord(char)
        if 97 <= o <= 122:
            result[o - 97] += 1
    mx = max(result)
    returns: str = []
    for i in range(26):
        if result[i] == mx:
            returns.append(chr(i + 97))
    return ''.join(returns)

if __name__ == '__main__':
    gets: list[str] = []
    for _i in range(50):
        gets.append(input().strip())
    print(compute(''.join(gets)))
