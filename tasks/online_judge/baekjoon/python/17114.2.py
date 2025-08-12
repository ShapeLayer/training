from collections import deque
input = iter(open(0).read().split('\n')).__next__

# optm: Tuples tend to perform better than lists in almost every category
# https://stackoverflow.com/questions/68630/are-tuples-more-efficient-than-lists-in-python
DT = (
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1)
)

# optm: Unwrap function call
# def compute(
#     field: list,
#     M: int, N: int, O: int, P: int, Q: int, R: int, S: int, T: int, U: int, V: int, W: int,
#     tomatoes: deque,
#     raw_tomato_counts: int
# ) -> int:
# 
#     elapsed = 1
#     q = tomatoes
# 
#     while q:
#         now = q.popleft()
# 
#         now_value = field[now[0]][now[1]][now[2]][now[3]][now[4]][now[5]][now[6]][now[7]][now[8]][now[9]][now[10]]
#         new_value = now_value + 1
# 
#         is_processed = False
# 
#         for dt in DT:
#             new = [now[i] + dt[i] for i in range(11)]
# 
#             if not (
#                 0 <= new[0] < W and
#                 0 <= new[1] < V and
#                 0 <= new[2] < U and
#                 0 <= new[3] < T and
#                 0 <= new[4] < S and
#                 0 <= new[5] < R and
#                 0 <= new[6] < Q and
#                 0 <= new[7] < P and
#                 0 <= new[8] < O and
#                 0 <= new[9] < N and
#                 0 <= new[10] < M
#             ):
#                 continue
# 
#             # if field[new[0]][new[1]][new[2]][new[3]][new[4]][new[5]][new[6]][new[7]][new[8]][new[9]][new[10]] == -1:
#             #     continue
# 
#             if field[new[0]][new[1]][new[2]][new[3]][new[4]][new[5]][new[6]][new[7]][new[8]][new[9]][new[10]] != 0:
#                 continue
# 
#             field[new[0]][new[1]][new[2]][new[3]][new[4]][new[5]][new[6]][new[7]][new[8]][new[9]][new[10]] = new_value
# 
#             raw_tomato_counts -= 1
# 
#             q.append(new)
#             is_processed = True
# 
#         if is_processed:
#             if elapsed < new_value:
#                 elapsed = new_value
# 
#     if raw_tomato_counts > 0:
#         return -1
#     return elapsed - 1

if __name__ == "__main__":
    M, N, O, P, Q, R, S, T, U, V, W = map(int, input().split())

    # ❯ python -mtimeit -s 'from collections import deque' -s 's = []' -s 'for _i in range(int(1e7)): s.append(0)'
    # 100000000 loops, best of 5: 3.79 nsec per loop
    # ❯ python -mtimeit -s 'from collections import deque' -s 's = deque()' -s 'for _i in range(int(1e7)): s.append(0)'
    # 100000000 loops, best of 5: 3.79 nsec per loop
    tomatoes = deque()
    
    # optm: Manage `0` value counts manually
    raw_tomato_counts = 0

    # optm: Reduce list.append call
    field = [[[[[[[[[[list(map(int, input().split())) for _n in range(N)] for _o in range(O)] for _p in range(P)] for _q in range(Q)] for _r in range(R)] for _s in range(S)] for _t in range(T)] for _u in range(U)] for _v in range(V)] for _w in range(W)]

    for w in range(W):
        for v in range(V):
            for u in range(U):
                for t in range(T):
                    for s in range(S):
                        for r in range(R):
                            for q in range(Q):
                                for p in range(P):
                                    for o in range(O):
                                        for n in range(N):
                                            for m in range(M):
                                                if field[w][v][u][t][s][r][q][p][o][n][m] == 1:
                                                    tomatoes.append((w, v, u, t, s, r, q, p, o, n, m))
                                                elif field[w][v][u][t][s][r][q][p][o][n][m] == 0:
                                                    raw_tomato_counts += 1

    # optm: Unwrap function call
    # print(compute(field, M, N, O, P, Q, R, S, T, U, V, W, tomatoes, raw_tomato_counts))
    # def compute:
    
    elapsed = 1
    q = tomatoes

    while q:
        now = q.popleft()

        now_value = field[now[0]][now[1]][now[2]][now[3]][now[4]][now[5]][now[6]][now[7]][now[8]][now[9]][now[10]]
        new_value = now_value + 1

        is_processed = False

        for dt in DT:
            new = [now[i] + dt[i] for i in range(11)]

            if not (
                0 <= new[0] < W and
                0 <= new[1] < V and
                0 <= new[2] < U and
                0 <= new[3] < T and
                0 <= new[4] < S and
                0 <= new[5] < R and
                0 <= new[6] < Q and
                0 <= new[7] < P and
                0 <= new[8] < O and
                0 <= new[9] < N and
                0 <= new[10] < M
            ):
                continue

            # if field[new[0]][new[1]][new[2]][new[3]][new[4]][new[5]][new[6]][new[7]][new[8]][new[9]][new[10]] == -1:
            #     continue

            if field[new[0]][new[1]][new[2]][new[3]][new[4]][new[5]][new[6]][new[7]][new[8]][new[9]][new[10]] != 0:
                continue

            field[new[0]][new[1]][new[2]][new[3]][new[4]][new[5]][new[6]][new[7]][new[8]][new[9]][new[10]] = new_value

            raw_tomato_counts -= 1

            q.append(new)
            is_processed = True

        if is_processed:
            if elapsed < new_value:
                elapsed = new_value

    if raw_tomato_counts > 0:
        print(-1)
    else:
        print(elapsed - 1)
