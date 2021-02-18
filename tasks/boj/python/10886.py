from sys import stdin

n = int(stdin.readline())
vote = [0, 0]
for _ in range(n):
    m = int(stdin.readline())
    if m:
        vote[1] += 1
    else:
        vote[0] += 1

if vote[0] > vote[1]:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')