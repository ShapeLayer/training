# 신발 섞어 신기
# array s non decreasing order (incresing and even)
# 정렬되어서 인풋
# 자신의 슈즈를 가질 수 없음
# 신발 사이즈는 자기 사이즈보다 이상
# * denoting a valid shuffling of shoes = 유효한 신발 셔플을 나타냅니다.

from sys import stdin
input = stdin.readline

for _t in range(int(input())):
    n = int(input())
    count = {}
    for i in map(int, input().split()):
        if i not in count: count[i] = 1
        else: count[i] += 1
    if 1 in count.values():
        print(-1)
        continue
    res = []
    latest = 0
    for i in count:
        res += [count[i]+latest]
        res += [j for j in range(latest+1, count[i]+latest)]
        latest = count[i]+latest
    print(' '.join(list(map(str, res))))