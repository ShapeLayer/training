table = {136: 1000, 142: 5000, 148: 10000, 154: 50000}
total = 0
for _i in range(int(input())):
    q, _ = map(int, input().split())
    total += table[q]
print(total)
