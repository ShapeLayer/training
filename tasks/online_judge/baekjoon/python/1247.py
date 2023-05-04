from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    for _i in range(3):
        n = int(input())
        s = 0
        for _j in range(n):
            s += int(input())
        if s == 0: print(0)
        else:
            print('+' if s > 0 else '-')
