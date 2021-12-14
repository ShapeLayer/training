def solution(participant, completion):
    for person in completion:
        participant.remove(person)
    answer = participant[0]
    return answer