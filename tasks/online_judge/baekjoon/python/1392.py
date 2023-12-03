from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n, q = map(int, input().split())
    gets = [int(input()) for _i in range(n)]
    for _i in range(q):
        t = int(input())
        for j in range(n):
            if t < sum(gets[:j + 1]):
                print(j + 1)
                break
