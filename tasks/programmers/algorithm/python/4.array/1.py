def solution(array, commands):
    answer = []
    for pattern in commands:
        arr = array[pattern[0]-1:pattern[1]]
        arr.sort()
        answer += [arr[pattern[2]-1]]
    return answer