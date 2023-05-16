from sys import stdin
while True:
    n = int(stdin.readline())
    if n == -1:
        break
    arr = [i for i in range(1, n//2+1) if n%i == 0]
    print('{} = {}'.format(n, ' + '.join(map(str, arr))) if sum(arr) == n else '{} is NOT perfect.'.format(n))
