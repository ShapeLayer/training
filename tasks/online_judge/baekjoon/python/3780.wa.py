from sys import stdin
input = stdin.readline

def compute(n: int, opers: list[list[int]]):
    parents: list[int] = [i for i in range(n + 1)]
    diff: list[int] = [0 for _i in range(n + 1)]
    
    def find(n: int) -> int:
        if n == parents[n]:
            return n
        parents[n] = find(parents[n])
        return parents[n]
    
    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa > pb:
            parents[pa] = pb
            parents[a] = pb
            diff[pb] += diff[pa] + a - b
            diff[pa] = 0
        elif pa < pb:
            parents[pb] = pa
            parents[b] = pa
            diff[pa] += diff[pb] + b - a
            diff[pb] = 0
    
    buf: list[int] = []
    for oper in opers:
        _type, params = oper[0], [*map(int, oper[1:])]
        if _type == 'E':
            buf.append(diff[find(params[0])])
        elif _type == 'I':
            merge(*params)
    return buf

if __name__ == '__main__':
    for _i in range(int(input())):
        n = int(input())
        opers: list[list[str]] = []
        while True:
            gets = input().split()
            if gets[0] == 'O':
                break
            else:
                opers.append(gets)
        print('\n'.join(map(str, compute(n, opers))))
