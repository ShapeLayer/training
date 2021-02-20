n = int(input())
f = int(input())
m = n - n%100

for i in range(m, m+100):
    if i % f == 0:
        print(str(i%100).zfill(2))
        break