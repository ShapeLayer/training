n = int(input())
s = input()
res = [0, 0]
for i in range(len(s)):
    if s[i] == 'A':
        res[0] += 1
    else:
        res[1] += 1
if res[0] > res[1]:
    print('A')
elif res[0] < res[1]:
    print('B')
else:
    print('Tie')