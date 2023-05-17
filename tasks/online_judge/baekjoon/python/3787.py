from sys import stdin
input = stdin.readline

def compute(n: int) -> tuple[int]:
    i = 0
    s = 0
    while True:
        i += 1
        s = i * (i + 1) /2
        if s >= n:
            break
    a = int(s - n + 1)
    b = int(i - (s - n))

    if i % 2 == 1:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    while True:
        gets = ''
        try:
            gets = input()
        except EOFError:
            break
        if not gets:
            break
        n = int(gets)
        a, b = compute(n)
        print(f'TERM {n} IS {a}/{b}')
