def solution(answers):
    cnt1, cnt2, cnt3, pnt = 0, 0, 0, [0, 0, 0]
    ans1, ans2, ans3 = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for ans in answers:
        if ans == ans1[cnt1]:
            pnt[0] += 1
        if ans == ans2[cnt2]:
            pnt[1] += 1
        if ans == ans3[cnt3]:
            pnt[2] += 1
        if cnt1 == 4:
            cnt1 = 0
        else:
            cnt1 += 1
        if cnt2 == 7:
            cnt2 = 0
        else:
            cnt2 += 1
        if cnt3 == 9:
            cnt3 = 0
        else:
            cnt3 += 1
    answer = []
    i = 0
    for pn in pnt:
        if pn == max(pnt):
            answer += [i+1]
        i += 1
    return answer