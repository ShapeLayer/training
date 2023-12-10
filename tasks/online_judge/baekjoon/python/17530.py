from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    gets = [int(input()) for _i in range(n)]
    print('S' if max(gets) == gets[0] else 'N')
