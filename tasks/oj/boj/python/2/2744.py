r = ''
for s in input():
    if ord('a') <= ord(s) <= ord('z'): r += chr(ord(s) - (ord('a') - ord('A')))
    elif ord('A') <= ord(s) <= ord('Z'): r += chr(ord(s) + (ord('a') - ord('A')))
print(r)