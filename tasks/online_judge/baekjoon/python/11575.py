from sys import stdin
input = stdin.readline

def compute(a: int, b: int, s: str) -> str:
    buf: list[str] = []
    for each in s:
        buf.append(chr(65 + ((ord(each) - 65) * a + b) % 26))
    return ''.join(buf)

if __name__ == '__main__':
    for _t in range(int(input())):
        a, b = map(int, input().split())
        s = input().strip()
        print(compute(a, b, s))
