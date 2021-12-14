import sys
while True:
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a)
    b = int(b)
    if a == 0 and b == 0:
        break
    print(a+b)