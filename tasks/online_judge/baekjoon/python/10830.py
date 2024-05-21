from sys import stdin
input = stdin.readline

dots = {}

def dot(n: int, a: list[list[int]], b: list[list[int]]):
    c = [[0 for _i in range(n)] for _j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % 1000
    return c

def compute(n: int, b: int, a: list[list[int]]):
    dots[1] = a
    dots[2] = dot(n, a, a)
    def step(depth: int):
        if depth in dots:
            return dots[depth]
        
        da = depth // 2
        db = depth - da
        dots[depth] = dot(n, step(da), step(db))
        return dots[depth]
    return step(b)

if __name__ == '__main__':
    n, b = map(int, input().split())
    a = [[*map(lambda each: int(each) % 1000, input().split())] for _i in range(n)]
    for row in compute(n, b, a):
        print(*row)
