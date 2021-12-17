def nref(num: int) -> int:
    num = 9
    return num

def nnoref(num: int) -> int:
    num = int(num)
    num = 14
    return num

n = 1
print('n', n, id(n))
print()

n_ = n
n_ += 1
print('n_', n_, id(n_))
print('n', n, id(n))
print('Same ID' if id(n) == id(n_) else 'Different ID')
print()

duplicated_n = n
duplicated_n = 10
print('duplicated_n', duplicated_n, id(duplicated_n))
print('n', n, id(n))
print('Same ID' if id(n) == id(duplicated_n) else 'Different ID')
print()

from copy import copy
copied_n = copy(n)
copied_n = 13
print('copied_n', copied_n, id(copied_n))
print('n', n, id(n))
print('Same ID' if id(n) == id(copied_n) else 'Different ID')
print()

addref_n = nref(n)
print('addref_n', addref_n, id(addref_n))
print('n', n, id(n))
print('Same ID' if id(n) == id(addref_n) else 'Different ID')
print()

addnoref_n = nnoref(n)
print('addnoref_n', addnoref_n, id(addnoref_n))
print('n', n, id(n))
print('Same ID' if id(n) == id(addnoref_n) else 'Different ID')
print()