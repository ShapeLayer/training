from sys import stdin
input = stdin.readline

def compute(n: int, gets: list[str]):
    h, v = 0, 0

    for row in gets:
        counts = 0
        for i in range(n):
            if row[i] == '.':
                counts += 1
            else:
                if counts >= 2:
                    h += 1
                counts = 0
        if counts >= 2:
            h += 1
    
    for k in range(n):
        col = [gets[j][k] for j in range(n)]
        counts = 0
        for i in range(n):
            if col[i] == '.':
                counts += 1
            else:
                if counts >= 2:
                    v += 1
                counts = 0
        if counts >= 2:
            v += 1
    
    return h, v

if __name__ == '__main__':
    n = int(input())
    gets = [input().strip() for _i in range(n)]
    print(*compute(n, gets))
