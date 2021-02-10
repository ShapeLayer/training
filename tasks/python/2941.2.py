from sys import stdin

txt = stdin.readline().rstrip()
defi = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for de in defi:
    txt = txt.replace(de, '0')

print(len(txt))