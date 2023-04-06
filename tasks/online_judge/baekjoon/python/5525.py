from sys import stdin
gets = stdin.readline
n = int(gets())
m = int(gets())
s = gets().rstrip()
string = 'I' + 'OI'*n
i = 0
counts = 0
lens = len(s)
lenstring = len(string)
for i in range(lens-lenstring):
    if s[i] == 'I':
        if s[i:i+lenstring] == string:
            counts += 1
print(counts)