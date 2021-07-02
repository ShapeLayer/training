# iterable: list, dict, set, str, bytes, tuple, range
a = {1, 2, 3, 4, 5, 6, 7}
b = iter(a)
while True:
    try:
        print(next(b))
    except StopIteration:
        break
