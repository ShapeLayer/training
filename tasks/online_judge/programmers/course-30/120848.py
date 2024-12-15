def solution(n):
    answer = 1
    fact = 1
    while fact <= n:
        answer += 1
        fact *= answer
    return answer - 1
