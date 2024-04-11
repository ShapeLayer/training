from collections import Counter
is_even = True
is_odd = True
for each in dict(Counter(list(input()))).values():
    if not is_even and not is_odd:
        break
    if each % 2 == 1:
        is_even = False
    if each % 2 == 0:
        is_odd = False

if is_even:
    print(0)
elif is_odd:
    print(1)
else:
    print(2)
