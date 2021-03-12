from sys import stdin
coms = dict(enumerate([[] for i in range(int(stdin.readline()))], start=1))
for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    coms[a] += [b]
    coms[b] += [a]
visited = []

def dfs(n):
    global visited
    visited += [n]
    for node in coms[n]:
        if node not in visited:
            dfs(node)

dfs(1)
print(len(visited)-1)