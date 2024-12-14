def solution(arr, n):
    answer = []
    
    is_len_even = len(arr) % 2 == 0
    for i in range(len(arr)):
        answer.append(
            arr[i] + (
                int(i % 2 == 1) * int(is_len_even) + \
                int(i % 2 == 0) * int(not is_len_even)
            ) * n
        )
    return answer
