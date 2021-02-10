from sys import stdin

while True:
    
    n1, n2 = list(map(int, stdin.readline().split()))
    if n1 == 0 and n2 == 0:
        break
    elif n1 % n2 == 0:
        print('multiple')
    elif n2 % n1 == 0:
        print('factor')
    else:
        print('neither')