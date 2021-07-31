n = int(input()) % 100
for i in range(1, 5):
    for j in [1, -1]:
        if j == 1:
            init, fina = 1, i+1
        else:
            init, fina = i, 0
        for k in range(init, fina, j):
            if n == 0:
                print(k if j == -1 else k-1)
            elif n < 5 and n > 0:
                print(k)
            n -= 5
