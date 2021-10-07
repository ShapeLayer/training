n = int(input())
p = list(map(int, input().split()))
avg = int(sum(p)/len(p))
avg_i = []
cnt = 0

for i in range(len(p)):
    if p[i] == avg:
        avg_i += [i]
print(avg)
for i in range(len(p)):
    for j in range(0, i+1):
        for avg_io in avg_i:
            print('i: {} j: {} bool: {} cnt: {}'.format(i, j, avg_io <= i and avg_io >= j, cnt))
            if avg_io <= i and avg_io >= j:
                cnt += 1
                is_in = True
print(cnt)
