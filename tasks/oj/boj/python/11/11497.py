from sys import stdin
input = stdin.readline

t = int(input())
for _t in range(t):
    n = int(input())
    logs = sorted(list(map(int, input().split())))
    replace = [-1] * n
    left, right = 0, -1
    for i in range(n // 2):
        if i != 0:
            prev_left, prev_right = replace[left-1], replace[right+1]
            if max(abs(prev_left - logs[2*i]), abs(prev_right - logs[2*i+1])) < max(abs(prev_left - logs[2*i+1]), abs(prev_right - logs[2*i])):
                replace[left] = logs[2*i]
                replace[right] = logs[2*i+1]
            else:
                replace[right] = logs[2*i]
                replace[left] = logs[2*i+1]
        else:
            replace[left] = logs[2*i]
            replace[right] = logs[2*i+1]
        left += 1
        right -= 1
    if n % 2 == 1:
        replace[n // 2] = logs[-1]
    max_delta = -1
    for i in range(n-1, -1, -1):
        dt = abs(replace[i] - replace[i-1])
        if dt > max_delta: max_delta = dt
    print(max_delta)