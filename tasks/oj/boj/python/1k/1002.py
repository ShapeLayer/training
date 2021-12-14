from sys import stdin

t = int(stdin.readline())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = list(map(int, stdin.readline().split()))
    if x1 == x2 and y1 == y2: # 두 원의 중심이 같은 경우
        if r1 == r2: # 두 원의 중심과 반지름이 같은 경우
            print(-1)
        else: # 두 원의 중심은 같으나 반지름이 다른 경우
            print(0)
    else:
        d = (abs(x1-x2)**2+abs(y1-y2)**2)**0.5
        if d == r1+r2: # 두 원의 중심 간의 거리가 반지름의 합과 같은 경우
            print(1)
        elif d > r1+r2: # 두 원의 중심 간의 거리가 반지름의 합보다 큰 경우
            print(0)
        else: # d < r1+r2 : 두 원의 중심 간의 거리가 반지름의 합보다 작은 경우
            R = 0 # 더 큰 반지름
            r = 0 # 더 작은 반지름
            if r1 > r2:
                R, r = r1, r2
            else:
                R, r = r2, r1
            if R == d+r: # 큰 원이 반지름이 중심 간 거리아 작은 원의 반지름의 합과 같은 경우
                print(1)
            elif R > d+r: # 큰 원이 반지름이 중심 간 거리아 작은 원의 반지름의 합보다 큰 경우
                print(0)
            else: # R < d+r : 큰 원이 반지름이 중심 간 거리아 작은 원의 반지름의 합보다 작은 경우
                print(2)