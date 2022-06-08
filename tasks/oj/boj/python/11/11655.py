gets = list(input())
for i in range(len(gets)):
    if ord('a') <= ord(gets[i]) <= ord('z'):
        gets[i] = chr((ord(gets[i]) - 97 + 13) % 26 + 97)
    elif ord('A') <= ord(gets[i]) <= ord('Z'):
        gets[i] = chr((ord(gets[i]) - 65 + 13) % 26 + 65)
print(''.join(gets))
