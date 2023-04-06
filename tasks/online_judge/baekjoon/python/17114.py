from collections import deque
# ^Z 로 입력 중단
input = iter(open(0).read().split('\n')).__next__

m, n, o, p, q, r, s, t, u, v, w = map(int, input().split())
storage = [[[[[[[[[[list(map(int, input().split())) for _n in range(n)] for _o in range(o)] for _p in range(p)] for _q in range(q)] for _r in range(r)] for _s in range(s)] for _t in range(t)] for _u in range(u)] for _v in range(v)] for _w in range(w)]
queue: deque = deque()
deltas = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]
]
'''
Data structure:
(time, _w, _v, _u, _t, ...)
'''
zero = 0
for _w in range(w):
    for _v in range(v):
        for _u in range(u):
            for _t in range(t):
                for _s in range(s):
                    for _r in range(r):
                        for _q in range(q):
                            for _p in range(p):
                                for _o in range(o):
                                    for _n in range(n):
                                        for _m in range(m):
                                            now = storage[_w][_v][_u][_t][_s][_r][_q][_p][_o][_n][_m]
                                            if now == 1:
                                                queue.append((0, _w, _v, _u, _t, _s, _r, _q, _p, _o, _n, _m))
                                            elif now == 0:
                                                zero += 1

elapsed = 0
while queue:
    now = queue.popleft()
    for dt in deltas:
        new = (now[0]+1, now[1]+dt[0], now[2]+dt[1], now[3]+dt[2], now[4]+dt[3], now[5]+dt[4], now[6]+dt[5], now[7]+dt[6], now[8]+dt[7], now[9]+dt[8], now[10]+dt[9], now[11]+dt[10])
        if 0 <= new[1] < w and 0 <= new[2] < v and 0 <= new[3] < u and 0 <= new[4] < t and 0 <= new[5] < s and 0 <= new[6] < r and 0 <= new[7] < q and 0 <= new[8] < p and 0 <= new[9] < o and 0 <= new[10] < n and 0 <= new[11] < m:
            if storage[new[1]][new[2]][new[3]][new[4]][new[5]][new[6]][new[7]][new[8]][new[9]][new[10]][new[11]] == 0:
                storage[new[1]][new[2]][new[3]][new[4]][new[5]][new[6]][new[7]][new[8]][new[9]][new[10]][new[11]] = 1
                zero -= 1
                queue.append(new)
                if new[0] > elapsed: elapsed = new[0]

if zero:
    print(-1)
else:
    print(elapsed)
