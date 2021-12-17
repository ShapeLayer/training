import numpy as np

def count(arr: np.array) -> dict:
    cnt = {}
    arr_1d = arr.flatten()
    for item in arr_1d:
        n = int(item)
        if n in cnt:
            cnt[n] += 1
        else:
            cnt[n] = 1
    return cnt

if __name__ == '__main__':
    # Result 1
    x = np.array([
        [10, 20, 40, 60],
        [10, 20, 40, 40]
    ], dtype=np.int32)
    print(x)
    d = count(x)
    for key in d:
        print('{} : {}번'.format(key, d[key]))
    print()
    # Result 2
    x = np.array([
        [80, 120, 40],
        [60, 80, 120],
        [40, 40, 40]
    ], dtype=np.int32)
    print(x)
    d = count(x)
    for key in d:
        print('{} : {}번'.format(key, d[key]))