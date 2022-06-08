gets = [sum(map(int, input().split())) for _i in range(5)]
m = max(gets)
for i in range(5):
    if m == gets[i]:
        print(i+1, gets[i])
