from sys import stdin
string = stdin.readline().rstrip()
alphabet = [-1 for i in range(26)]

for i in range(len(string)):
    o = ord(string[i])
    if alphabet[o-97] == -1:
        alphabet[o-97] = i

print(' '.join(list(map(str, alphabet))))