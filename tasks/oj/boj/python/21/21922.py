## 시간초과: 디버그 코드로 m, n이 큰 수인 연구실 맵 생성 후 추가... 
## 오래 걸림
from sys import stdin
lab = []
conditioners = []
airpath = set()

n, m = map(int, stdin.readline().split())
for y in range(n):
    arr = list(map(int, stdin.readline().split()))
    if 9 in arr:
        for x in range(m):
            if arr[x] == 9:
                conditioners += [(y, x)]
    lab += [arr]

for conditioner in conditioners:
    for direction in range(4): # up right down left
        f = conditioner # focus
        back = False
        if direction == 0:
            offset = [-1, 0]
        elif direction == 1:
            offset = [0, 1]
        elif direction == 2:
            offset = [1, 0]
        else:
            offset = [0, -1]
        d = direction
        while not back:
            airpath.add(f)
            ns = (f[0]+offset[0], f[1]+offset[1]) # next_step
            if ns[0] >= 0 and ns[1] >= 0 and ns[0] < n and ns[1] < m:
                if lab[ns[0]][ns[1]] == 0:
                    pass
                elif lab[ns[0]][ns[1]] == 1:
                    if d == 1 or d == 3:
                        airpath.add(ns)
                        back = True
                elif lab[ns[0]][ns[1]] == 2:
                    if d == 0 or d == 2:
                        airpath.add(ns)
                        back = True
                elif lab[ns[0]][ns[1]] == 3:
                    if d == 0:
                        d = 1
                        offset = [0, 1]
                    elif d == 1:
                        d = 0
                        offset = [-1, 0]
                    elif d == 2:
                        d = 3
                        offset = [0, -1]
                    elif d == 3:
                        d = 2
                        offset = [1, 0]
                elif lab[ns[0]][ns[1]] == 4:
                    if d == 0:
                        d = 3
                        offset = [0, -1]
                    elif d == 1:
                        d = 2
                        offset = [1, 0]
                    elif d == 2:
                        d = 1
                        offset = [-1, 0]
                    elif d == 3:
                        d = 0
                        offset = [0, 1]
                else:
                    airpath.add(ns)
                    back = True
                f = ns
            else:
                back = True
print(len(airpath))
