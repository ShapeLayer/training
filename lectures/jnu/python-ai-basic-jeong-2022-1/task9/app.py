# 문제 제시 값
from datetime import datetime
dayNum = datetime.today().day

# 5부제 표 만들기
datetable = {}
for i in range(1, 32): # 최대 31일까지
    n = (i % 10) % 5
    datetable[i] = [n, n+5]

gets = int(input('차량 번호 4자리를 입력하세요: '))
print('--------------------------')
print(f'오늘 날짜: {dayNum}일')
print(f'출입 가능 차량 끝자리 번호: {datetable[dayNum][0]}, {datetable[dayNum][1]}')
print('--------------------------')
if gets % 10 in datetable[dayNum]:
    print('귀하의 차는 출입 가능합니다!!!')
else:
    print('귀하의 차는 출입 불가합니다!!!')
