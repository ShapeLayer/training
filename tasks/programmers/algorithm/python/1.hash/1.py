def solution(participant, completion):
    hash = {}
    for person in participant:
        try:
            hash[person] += 1
        except KeyError:
            hash[person] = 1
    for person in completion:
        hash[person] -= 1

    answer = ''
    for person in hash:
        if hash[person] != 0:
            answer = person
    return answer