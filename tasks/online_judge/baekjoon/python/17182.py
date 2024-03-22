from sys import stdin
input = stdin.readline

visits = []
result = 1e10

def compute(n, k, adj):
    global visits
    dist = [[each for each in row] for row in adj]

    for i in range(n):
        for j in range(n):
            for _k in range(n):
                dist[i][j] = min(dist[i][j], dist[i][_k] + dist[_k][j])

    visits = [False for i in range(n)]

    def explore(depth, _from, costs, v):
        global result
        if depth == n:
            result = min(costs, result)
            return
        for i in range(n):
            if visits[i]:
                continue
            visits[i] = True
            v.append(i)
            explore(depth + 1, i, costs + dist[_from][i], v)
            v.pop()
            visits[i] = False

    visits[k] = True
    explore(1, k, 0, [k])

    return result

if __name__ == '__main__':
    n, k = map(int, input().split())
    adj = [[*map(int, input().split())] for _i in range(n)]
    print(compute(n, k, adj))
