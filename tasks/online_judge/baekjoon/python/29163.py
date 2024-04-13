_, arr = input(), map(int, input().split())
counts = [0, 0]
for each in arr:
    counts[each % 2] += 1

print('Happy' if counts[0] > counts[1] else 'Sad')
