arr = []
for i in range(5):
    arr += [int(input('성적을 입력하시오 : '))]
print('성적 평균은 {} 입니다.'.format(sum(arr)/5))
over_70 = 0
for i in arr:
    if i >= 70:
        over_70 += 1
print('70점 이상 성적을 받은 학생은 {} 명 입니다.'.format(over_70))