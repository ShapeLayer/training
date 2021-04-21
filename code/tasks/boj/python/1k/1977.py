from math import ceil, floor
m = int(input())
n = int(input())
c = ceil(m**0.5)

arr = []
while True:
    mm = int(c**2)
    if mm <= n: 
        arr += [mm]
        c += 1
        continue
    break
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))