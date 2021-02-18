def solution(array, commands):
    answer = []
    for pattern in commands:
        arr = array[pattern[0]-1:pattern[1]]
        arr.sort()
        answer += [arr[pattern[2]-1]]
    return answer

# 테스트 케이스는 통과했으나, 제출 후 채점하기 처리 시 서버 내부 오류가 발생함.
'''
정확성  테스트:
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
'''