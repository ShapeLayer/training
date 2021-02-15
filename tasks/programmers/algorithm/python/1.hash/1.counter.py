import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    # 남은 인원이 없으면 카운트가 0이 되는 것이 아니라 그냥 삭제됨
    return list(answer.keys())[0]