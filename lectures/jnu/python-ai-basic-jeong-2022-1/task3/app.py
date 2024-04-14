# 문제에서 제시한 값
# 딕셔너리 사용법: {key: value, key: value, ...}
score_cuts = {
    'A+': 4.5,
    'A': 4.0,
    'B+': 3.5,
    'B': 3.0, 
    'C+': 2.5,
    'C': 2.0,
    'D+': 1.5,
    'D': 1.0,
    'F': 0
}

# PPT에서 제시한 예시값
# 학점이 문자로 표기되어 있으므로, 문자로 저장
# 과목명에 따라 학점을 기록해야 하므로 딕셔너리 사용
scores = {
    'C': 'A',
    'Java': 'F',
    '모바일': 'C',
    '보안': 'A+',
    '해킹': 'F',
    '파이썬': 'A',
    'os': 'A+'
}

# 정수형 변수 선언: 합계 기록
# 반복문을 사용하여 서서히 더해갈 것이므로 0으로 초기화
sums = 0

# 딕셔너리는 이터레이터이므로 반복문 사용 가능
# 이때 lecture는 딕셔너리의 key값이 할당됨
for lecture in scores:
    # 합계 기록할 변수에 "반복문에서 현재 확인하고 있는 과목의 점수" 덧셈
    # lecture: 과목명
    # scores[lecture]: 과목의 학점
    # score_cuts[scores[lecture]]: 과목의 학점을 숫자로 변환
    sums += score_cuts[scores[lecture]]
    # "반복문에서 현재 확인하고 있는 과목"의 정보를 출력
    # 출력은 f-string을 사용함
    # \t: tab키 만큼 띄워쓰기, PPT처럼 예쁘게 공백을 넣을 때 활용
    # f-string은 {}(중괄호) 내부를 일반 파이썬 코드처럼 사용 가능함
    print(f'{lecture}\t: {scores[lecture]}')

# 결과 출력
# 실수형 자릿수 맞추기 용이하도록 % 포맷 사용
print('중간고사 학점: %.1f' % (sums/len(scores)))
