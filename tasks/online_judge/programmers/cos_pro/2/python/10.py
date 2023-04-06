def solution(arr, k):
    u = []
    for i in arr:
        u += i
    u.sort()
    return u[k-1]