from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    gets = -1
    while True:
        try:
            gets = int(input())
        except (EOFError, ValueError):
            break
        val, res = 1, 1
        while True:
            if val % gets == 0: break
            else:
                res += 1
                val = (val * 10 + 1) % gets
        print(res)
