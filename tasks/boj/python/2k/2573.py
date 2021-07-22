from sys import stdin
berg = []

def processing():
    next_berg = berg
    for y in range(n):
        for x in range(m):
            cnt = 0
            for offset in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if y+offset[0] >= 0 and x+offset[1] >= 0 and y+offset[0] < n and x+offset[1] < m:
                    if next_berg[y+offset[0]][x+offset[1]] == 0:
                        cnt += 1
            next_block = berg[y][x] - cnt
            next_berg[y][x] = 0 if next_block < 0 else next_block
    return next_berg
    
def checking():
    group = []
    for y in range(n):
        for x in range(m):
            if berg[y][x] != 0:
                near = []
                for offset in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if y+offset[0] >= 0 and x+offset[1] >= 0 and y+offset[0] < n and x+offset[1] < m:
                        for i in range(len(group)):
                            if [y+offset[0], x+offset[1]] in group[i]:
                                near += [i]
                        if not near:
                            group += [[y, x]]
                        elif len(near) == 1:
                            group[near[0]] += [[y, x]]
                        else:
                            init = near[0]
                            for a in range(len(near)):
                                if a == 0:
                                    continue
                                group[init] += group.pop(near[a]-(a-1))
                                group[init] += [[y, x]]
            # print(group)
    print(group)
    if len(group) > 1:
        return True
    else:
        return False

n, m = map(int, stdin.readline().split())
for _ in range(n):
    berg += [list(map(int, stdin.readline().split()))]
print(berg)
print(checking())
y = 0
while not checking():
    berg = processing()
    y += 1
    print(checking())
print(y)
