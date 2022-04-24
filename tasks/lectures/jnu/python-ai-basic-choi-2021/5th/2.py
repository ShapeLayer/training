languages = ['java', 'java', '#c', 'java', 'java', 'c/c++', 'java']
print('주어진 리스트는 다음과 같습니다.')
print(languages)
new_langs = []
deathnote = input('지울 단어를 입력하세요: ')
for l in languages:
    if l != deathnote:
        new_langs += [l]
print('%s를 모두 지웠습니다.' %deathnote)
print(new_langs)