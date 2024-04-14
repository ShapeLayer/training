for n in range(2, 13):
    for m in range(2, n+1):
        if n%m == 0:
            if n == m:
                print('{} : 소수'.format(n))
            else:
                print('{} : 합성수'.format(n))
                break