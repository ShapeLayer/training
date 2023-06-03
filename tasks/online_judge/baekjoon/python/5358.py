from sys import stdin
input = stdin.readline

def compute(name: str) -> str:
    buf: list[str] = []
    for char in name:
        if char == 'i':
            buf.append('e')
        elif char == 'e':
            buf.append('i')
        elif char == 'I':
            buf.append('E')
        elif char == 'E':
            buf.append('I')
        else:
            buf.append(char)
    return ''.join(buf)

if __name__ == '__main__':
    gets = ''
    while True:
        try:
            gets = input()
        except EOFError:
            break
        gets = gets.strip()
        if not gets:
            break
        print(compute(gets))
