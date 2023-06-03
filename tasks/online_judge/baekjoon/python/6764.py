def compute(arr: list[int]) -> str:
    if arr[0] < arr[1] and arr[1] < arr[2] and arr[2] < arr[3]:
        return 'Fish Rising'
    elif arr[0] > arr[1] and arr[1] > arr[2] and arr[2] > arr[3]:
        return 'Fish Diving'
    elif max(arr) == min(arr):
        return 'Fish At Constant Depth'
    else:
        return 'No Fish'

if __name__ == '__main__':
    print(compute([int(input()) for _i in range(4)]))
