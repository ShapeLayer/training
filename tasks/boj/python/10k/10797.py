date = int(input())
cars = list(map(int, input().split()))

cnt = 0
for car in cars:
    if car == date:
        cnt += 1
print(cnt)