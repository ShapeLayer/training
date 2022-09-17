gets = [0] * 8
for i in range(8):
    gets[i] = int(input())
s = sorted(gets, reverse=True)[:5]
puts = []
print(sum(s))
for i in range(8):
    if gets[i] in s: puts += [i+1]
print(' '.join(map(str, puts)))
