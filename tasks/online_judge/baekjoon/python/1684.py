from sys import stdin
input = stdin.readline

def compute(n: int, gets: list[int]):
    r = None
    for d in range(max(gets), 0, -1):
        flag = True
        for n in gets:
            if r == None:
                r = n % d
            elif r != n % d:
                flag = False
                r = None
                break
        if flag:
            return d

if __name__ == '__main__':
    n = int(input())
    gets = [*map(int, input().split())]
    print(compute(n, gets))
