n = int(input())
arr = list(map(int, input().split()))
budget = int(input())

m = min(arr)
M = max(arr)
limit = [0, (m*n + M*n) // 2]
latest = 0

def sum_budgets():
    ## Sum Budgets
    s = 0
    for n in arr:
        if n > limit[1]:
            s += limit[1]
        else:
            s += n
    return s

def step():
    global m, M, latest, limit
    s = sum_budgets()
    while True:
        print('budget: {}, latest: {}, s: {}, M: {}, m: {}, limit: {}'.format(budget, latest, s, M, m, limit))
        if s > budget:
            #if latest and latest < budget: # 하자 발생
            #    return latest
            M = limit[1]
            latest = s
        elif s < budget:
            if latest == s:
                return latest
            m = limit[1]
            latest = s
        else:
            return s
        limit[0] = limit[1]
        limit[1] = (m*n + M*n) // 2
        s = sum_budgets()

print(step())
print(limit[0])