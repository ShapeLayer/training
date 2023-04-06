def chk(n):
    cnt = 0
    for i in range(1, n//3+1):
        for j in range(i, 2*(n//3)+1):
            k = n - (i + j)
            if k < j:
                break
            if i + j > k:
                cnt += 1
    return cnt

print(chk(int(input())))