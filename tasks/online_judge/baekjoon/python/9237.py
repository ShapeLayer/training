from sys import stdin
input = stdin.readline

def compute(N: int, T: list):
    T.sort(reverse=True)

    grow_done = [-1 for _i in range(N)]
    for i in range(N):
        grow_done[i] = T[i] + (i + 1) + 1
    
    return max(grow_done)


if __name__ == "__main__":
    N = int(input())
    T = [*map(int, input().split())]
    print(compute(N, T))
