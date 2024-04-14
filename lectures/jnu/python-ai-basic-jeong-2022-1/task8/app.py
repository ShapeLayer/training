text = '''Success is not the key to happiness.
Happiness is the key to success.
If you love what you are doing, you will be successful.
- Albert Schweitzer'''

text = text.replace(' ', '') # ' '(공백)을 ''(없음)으로 대체 => 공백 제거
# 아래 주석 제거해서 어떻게 바뀌었나 확인하기
# print(text)
text = text.replace('\n', '') # '\n'(개행)을 ''(없음)으로 대체 => 개행 제거
# 아래 주석 제거해서 어떻게 바뀌었나 확인하기
# print(text)
text = text.lower() # 대소문자를 구분하지 않기 위해 문장 전체를 소문자로 변경함
# 아래 주석 제거해서 어떻게 바뀌었나 확인하기
# print(text)
counts = {} # 글자 수 세서 결과 기록할 딕셔너리 생성, 빈 상태로 유지
for alphabet in text:
    # text에서 문자 하나씩을 뽑아서 alphabet에 할당
    # 앞에서부터 한문자씩 뽑고,
    # 반복할때마다 다음 문자를 뽑아냄

    # 아래 주석 제거해서 어떻게 바뀌었나 확인하기
    # print(alphabet)
    if alphabet not in counts: # 글자 수 기록에 지금의 문자(alphabet)가 없다면
        counts[alphabet] = 1   # 글자 수 기록에 지금의 문자 추가 (1개)
    else:                      # 그게 아니라면 (= 글자 수 기록에 지금의 문자가 있다면)
        counts[alphabet] += 1  # 글자 수 기록에 지금의 문자 개수 기록 1 올리기
    # 아래 주석 제거해서 어떻게 바뀌었나 확인하기
    # print(counts)

for key in sorted(counts):     # 순서대로 counts의 키 값(=alphabet)을 key 변수에 담음
    print('{} --> {}'.format(key, counts[key])) # 결과 출력