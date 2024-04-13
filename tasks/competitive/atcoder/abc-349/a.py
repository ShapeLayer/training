from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    input()
    print(sum(map(int, input().split())) * -1)
