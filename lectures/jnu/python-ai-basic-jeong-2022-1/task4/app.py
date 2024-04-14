# 문제 제시 코드
scores = [] # 성적 저장을 위한 리스트
weight = [.1, .2, .3, .4] # 가중치 리스트

for i in range(1, 5):
    value = int(input(str(i) + '차 성적 입력 : '))
    scores.append(value)
# 문제 제시 코드 끝

# 실수형 변수 선언: 합계 기록
# 반복문을 사용하여 서서히 더해갈 것이므로 0.0으로 초기화
sums = .0

# 4회 반복, i는 0~3
for i in range(4):
    # 가중치 연산 결과를 변수에 저장
    # : 반복문 코드 스코프 내에서 2회 이상 사용되므로 변수 사용
    # i를 scores와 weight의 인덱스 키로 사용 가능
    weighted = scores[i] * weight[i]
    # 합계 기록할 변수에 가중치 연산 결과 덧셈
    sums += weighted
    # 결과 출력
    # 실수형 자릿수 간편하게 맞출 수 있도록 % 포맷 사용
    print('%d차 점수 : %d -> %.1f' % (i+1, scores[i], weighted))

# 실수형 자릿수 간편하게 맞출 수 있도록 % 포맷 사용
print('점수 = %.2f' % sums)
