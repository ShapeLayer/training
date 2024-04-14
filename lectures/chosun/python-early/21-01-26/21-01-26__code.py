# 1번문제
lang = 'python'

## 답:
print(lang[0], lang[2])


# 2번문제
license_plate = '24가 2210'

## 답:
print(license_plate.split()[1])


# 3번문제
string = '홀짝홀짝홀짝'

## 답:
print(string.replace('짝', ''))


# 4번문제
string = 'PYTHON'

## 답
print(string[::-1])


# 5번 문제 / 6번 문제
phone_number = '010-1111-2222'

## 5번 답
print(phone_number.replace('-', ' '))
## 6번 답
print(phone_number.replace('-', ''))


# 7번 문제
## 예상 답안: Python 이 출력됨
##  * python 문자열의 첫 문자를 P로 변경
'''
lang = 'python'
lang[0] = 'P'
print(lang)
'''

## 결과: 오류
##  TypeError: 'str' object does not support item assignment
##  > String 자료형은 인덱싱 결과를 다시 할 수 없음
##    해결방법: 리스트로 바꿨다가 변경 후 다시 문자열화
lang = 'python'
lang = list(lang)
lang[0] = 'P'
lang = ''.join(lang)
print(lang)


# 8번 문제
string = 'abcdfe2a354a32a'

## 답
print(string.replace('a', 'A'))


# 9번 문제
## 답: aBcd 가 출력됨
##  * .replace() 함수를 통해 b를 B로 변경
string = 'abcd'
string.replace('b', 'B')
print(string)


# 10번 문제 / 11번 문제 / 12번 문제
## 10번 답
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)
## 11번 답
movie_rank += ['배트맨']
print(movie_rank)
## 12번 답
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)
## 13번 답
movie_rank.remove('럭키')
print(movie_rank)
## 14번
movie_rank.remove('스플릿')
movie_rank.remove('배트맨')
print(movie_rank)



# 15번 문제
lang1 = ['C', 'C++', 'JAVA']
lang2 = ['Python', 'Go', 'C#']

## 답:
langs = lang1 + lang2
print(langs)


# 16번 문제:
nums = [1, 2, 3, 4, 5, 6, 7]

## 답
print('max: {}'.format(max(nums)))
print('min: {}'.format(min(nums)))


# 17번 문제:
nums = [1, 2, 3, 4, 5]

## 답
print(sum(nums))


# 18번 문제
cook = ['피자', '김밥', '만두', '양념치킨', '족발', '피자', '김치만두', '쫄면', '소세지', '라면', '팥빙수', '김치전']

## 답
print(len(cook))


# 19번 문제
nums = [1, 2, 3, 4, 5]

## 답
print(sum(nums, 0) / len(nums))


# 20번 문제
price = ['20180728', 100, 130, 140, 150, 160, 170]

## 답
print(price[1:])


# 21번 문제 / 22번 문제
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## 21번 답
print(nums[::2])
## 22번 답
print(nums[1::2])


# 23번 문제
nums = [1, 2, 3, 4, 5]

## 답
print(nums[::-1])


# 24번 문제
interest = ['삼성전자', 'LG전자', 'Naver']

## 답
print(interest[0], interest[2])


# 25번 문제 / 26번 문제
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

## 25번 답
print(' '.join(str(i) for i in interest))
## 26번 답
print('/'.join(str(i) for i in interest))