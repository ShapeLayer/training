from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    for _i in range(int(input())):
        n, d, a, b, f = map(float, input().split())
        t = d / (a + b) * f
        print(int(n), t)
