e, s, m, y = map(int, input().split() + [1])
while (y - e) % 15 != 0 or (y - s) % 28 != 0 or (y - m) % 19 != 0:
    y += 1
print(y)