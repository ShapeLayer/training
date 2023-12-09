from sys import stdin
input = stdin.readline

def compute(n: int, m: int, forces: list[int], activities: list[list[int]]):
    parents = [i for i in range(n + 1)]
    
    def find(n: int) -> n:
        if n == parents[n]:
            return n
        parents[n] = find(parents[n])
        return parents[n]
    
    def merge(a: int, b: int, _type: int):
        pa, pb = find(a), find(b)
        force = forces[pa] + forces[pb] if _type == 1 else abs(forces[pa] - forces[pb])
        if pa > pb:
            parents[pa] = pb
            parents[a] = pb
            forces[pa] = 0
            forces[pb] = force
        else:
            parents[pb] = pa
            parents[b] = pa
            forces[pb] = 0
            forces[pa] = force
    
    for o, p, q in activities:
        merge(p, q, o)

    survived = []
    for each in forces:
        if each != 0:
            survived.append(each)
    return survived

if __name__ == '__main__':
    n, m = map(int, input().split())
    forces = [0] + [int(input()) for _i in range(n)]
    activities = [[*map(int, input().split())] for _i in range(m)]
    survived = compute(n, m, forces, activities)
    print(len(survived))
    print(*sorted(survived))
