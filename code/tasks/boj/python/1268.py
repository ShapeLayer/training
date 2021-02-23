stds = int(input())
std_cls = []
std_same = [set() for _ in range(stds)]
for _ in range(stds):
    std_cls += [list(map(int, input().split()))]
for g in range(5):
    for i in range(stds):
        for j in range(stds-i):
            if std_cls[i][g] == std_cls[i+j][g]:
                std_same[i].add(i+j+1)
                std_same[i+j].add(i+1)
std_same_arr = []
for std in std_same:
    std_same_arr += [len(std)]
print(std_same_arr.index(max(std_same_arr))+1)