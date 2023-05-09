from sys import stdin
input = stdin.readline

def compute(real: list[int], argue: list[int]):
    d = {r: True for r in real}
    for a in argue:
        if a in d and d[a]:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        real = list(map(int, input().split()))
        m = int(input())
        argue = list(map(int, input().split()))
        compute(real, argue)
