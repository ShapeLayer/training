def slice_rc(arr: list, h: int, m: int):
    margin = 0
    while m > margin:
        h -= 1
        margin = 0
        for rc in arr:
            if rc > h:
                margin += rc - h
    return h

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(slice_rc(arr, max(arr), m))