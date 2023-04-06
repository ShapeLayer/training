a, b = input(), input()
s = ''
for i in range(8):
    s += a[i]+b[i]
while len(s) > 2:
    n = ''
    for i in range(len(s)-1):
        n += str((int(s[i]) + int(s[i+1])) % 10)
    s = n
print(n)
