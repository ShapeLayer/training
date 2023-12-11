from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    while True:
        a, b = map(int, input().split())
        if a == b == 0: break
        print(a - (b - a))
