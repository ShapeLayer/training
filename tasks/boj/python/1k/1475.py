from collections import Counter
from math import ceil

c = dict(Counter(input()))
if '6' in c and '9' in c:
    c['6'] += c['9']
elif '9' in c:
    c['6'] = c['9']

if '9' in c:
    c['9'] = 0
if '6' in c:
    c['6'] = ceil(c['6'] / 2)

print(max(c.values()))
