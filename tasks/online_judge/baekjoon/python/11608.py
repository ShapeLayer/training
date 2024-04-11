from collections import Counter
c = dict(Counter(input()))
c['_'], c['__'] = 0, 0
print(sum([c[key] for key in sorted(c, key=lambda each: c[each], reverse=True)[2:]]))
