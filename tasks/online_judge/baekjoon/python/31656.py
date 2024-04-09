buf = []
prev = None
for each in input():
    if each != prev:
        prev = each
        buf.append(each)
print(''.join(buf))
