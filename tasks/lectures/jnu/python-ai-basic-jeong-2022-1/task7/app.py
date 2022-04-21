# 현재 날짜 = 2022년
now = 2022

# 내년에도 내후년에도 코드 잘 실행해보기
# datetime 클래스 임포트
from datetime import datetime
# datetime.now()는 결과로 datetime형을 반환함.
# datetime에서 year month day 등을 가져올 수 있음
now = datetime.now().year

# 문제 제시 값
id = '881120-1000000'
# id[:2]는 id 변수의 앞 두 문자를 가져오므로 88을 가져올 수 있음
# id[:2]는 문자열이므로 문자열 '19'와 합친 뒤 int로 변환
year = int('19'+id[:2]) # borns

# 문제 제시 알고리즘
age = now - year

# 결과
print('----------------------------')
print(f'홍길동은 {year}년도에 태어났다.')
print(f'홍길동의 나이는 만 {age} 이다.')
print('----------------------------')
