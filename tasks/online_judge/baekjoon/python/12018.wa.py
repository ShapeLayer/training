from sys import stdin
input = stdin.readline

class Class:
    def __init__(self, p: int, l: int, puts: list[int]):
        self.p = p
        self.l = l
        self.puts = sorted(puts)
        self.req = puts[p - l] if p - l >= 0 else 1

def compute(n: int, m: int, classes: list[Class]):
    result = []
    classes.sort(key=lambda each: each.req)
    for each in classes:
        m -= each.req
        if m >= 0:
            result.append(each)
        else:
            break
    return len(result)

n, m = map(int, input().split())
classes = []
for _i in range(n):
    p, l = map(int, input().split())
    puts = [*map(int, input().split())]
    classes.append(Class(p, l, puts))

print(compute(n, m, classes))
