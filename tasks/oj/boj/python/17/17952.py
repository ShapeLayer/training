stack = [] # [score, duration]
score = 0
for m in range(1, int(input()) + 1):
    gets = list(map(int, input().split()))
    if gets == [0]:
        if stack:
            stack[-1][1] -= 1
            if stack[-1][1] == 0:
                done = stack.pop()
                score += done[0]
    else:
        q, a, t = gets
        if t == 1:
            score += a
        else:
            stack += [[a, t-1]]
print(score)