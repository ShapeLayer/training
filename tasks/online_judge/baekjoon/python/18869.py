m, n = map(int, input().split())
univ_origin = [list(map(int, input().split())) for _i in range(m)]
univ_comps = []
for univ in univ_origin:
    conn = {}
    sort = sorted(univ)
    prev = None
    offset = 0
    for i in range(n):
        if prev != None:
            if prev == sort[i]:
                offset += 1
        prev = sort[i]
        conn[sort[i]] = i - offset
    univ_comps.append(list(map(lambda x: conn[x], univ)))

cnt = 0
for i in range(m):
    for j in range(m):
        if i <= j: continue
        if univ_comps[i] == univ_comps[j]: cnt += 1

print(cnt)
