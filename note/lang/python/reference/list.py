def addref(ll: list) -> list:
    ll.append(9)
    return ll

def addnoref(ll: list) -> list:
    copied_ll = list(ll)
    copied_ll.append(9)
    return copied_ll

arr = [1, 3, 5, 6]
print('arr', arr, id(arr))
print()

print('arr', arr, id(arr))
bf_id = id(arr)
arr = [3, 5, 6, 7]
print('arr', arr, id(arr))
print('Same ID' if id(arr) == bf_id else 'Different ID')
print()

duplicated_arr = arr
duplicated_arr.append(10)
print('duplicated_arr', duplicated_arr, id(duplicated_arr))
print('arr', arr, id(arr))
print('Same ID' if id(arr) == id(duplicated_arr) else 'Different ID')
print()

from copy import copy
copied_arr = copy(arr)
copied_arr.append(13)
print('copied_arr', copied_arr, id(copied_arr))
print('arr', arr, id(arr))
print('Same ID' if id(arr) == id(copied_arr) else 'Different ID')
print()

addref_arr = addref(arr)
print('addref_arr', addref_arr, id(addref_arr))
print('arr', arr, id(arr))
print('Same ID' if id(arr) == id(addref_arr) else 'Different ID')
print()

addnoref_arr = addnoref(arr)
print('addnoref_arr', addnoref_arr, id(addnoref_arr))
print('arr', arr, id(arr))
print('Same ID' if id(arr) == id(addnoref_arr) else 'Different ID')
print()