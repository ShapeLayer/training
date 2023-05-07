from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    for _i in range(int(input())):
        print(sum(map(int, input().split())))
