t = [False for _i in range(31)]
for i in range(28): t[int(input())] = True
for i in range(1, 31):
    if not t[i]: print(i)