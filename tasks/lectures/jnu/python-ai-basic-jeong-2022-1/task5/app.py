# 문제 제시 값
from cv2 import split


text = 'Life is too short, you need python'

# 파이썬의 print() 함수는 형식이 달라도 ,로 나눠서 넣으면 알아서 잘 출력됨
print('전체 문자의 수:', len(text))

# 공백 제거하기: text.replace(target, to)
# target 문자를 to로 변경
# text 변수 값을 직접 바꾸는 것이 아니고 결과가 text.replace()에서 치환되는것과 동일하게 작동
# 결과적으로 그 자체가 값으로 취급되므로 text = text.replace()를 해서 결과를 다시 변수에 반영해야함
replaced = text.replace(' ', '')
print('공백을 제외한 문자의 수:', len(replaced))

# 단어의 수 = 공백을 기준으로 나눈 결과들의 개수
# text.split()는 변수 값을 직접 바꾸는 것이 아니고 결과가 치환되는 것과 동일하게 작동
# text.split()의 결과는 리스트임: len() 사용 가능함
print('단어의 수:', len(text.split()))

# index(string)으로 인덱스 확인 가능
print('python의 인덱스', text.index('python'))

# 첫 글자만 대문자로 만들기
# 1. split()으로 공백 기준으로 분할: 결과는 리스트
splited = text.split()
# 2. 반복문을 사용해서 각 리스트 아이템의 첫 문자를 대문자로 변경
for i in range(len(splited)):
    splited[i] = splited[i][0].upper() + splited[i][1:]
# 3. 리스트를 문자열로 전환하여 출력
print('첫 글자만 대문자로: ' + ' '.join(splited))

# 문자열 거꾸로 출력하기: 문자열 슬라이싱 사용
print('문자열을 거꾸로 출력: ' + text[::-1])