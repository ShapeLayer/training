def solution(arr):
    answer = []
    for i in range(len(arr)):
        now = arr[i]
        if now >= 50 and now % 2 == 0:
            answer.append(now // 2)
        elif now < 50 and now % 2 == 1:
            answer.append(now * 2)
        else:
            answer.append(now)
    return answer
