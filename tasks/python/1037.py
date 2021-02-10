from sys import stdin
t = int(stdin.readline())
ns = list(map(int, stdin.readline().split()))
ns.sort() # 수를 오름차순/내림차순으로 제시한다는 조건이 없었음

if t % 2 == 0: #len == even
    print(ns[(t//2)-1] * ns[t//2])
    #print(ns[0] * ns[t-1])
else: #len == odd
    print(ns[(t//2)] ** 2)
    #print(ns[0] * ns[t-1])