# 1
movie_1 = ['명탐정 코난: 감청의 권', 2019, '애니메이션', '일본어', '전설의 보물 "블루 사파이어"를 둘러싼 배틀 미스터리', 0, False]
movie_2 = ['명탐정 코난: 제로의 집행인', 2018, '애니메이션', '일본어', '진실을 파헤치는 자 vs 정의를 관철하는 자', 0, False]
movie_3 = ['명탐정 코난: 진홍의 연가', 2017, '애니메이션', '일본어', '두 운명을 갈라놓은 슬픈 노래, 붉게 물든 미스터리 로맨스', 0, False]
movie_4 = ['명탐정 코난: 순흑의 악몽', 2016, '애니메이션', '일본어', '밝혀진 더블 페이스! 숙명이 이끄는 정상대결 미스터리', 0, False]
movie_5 = ['명탐정 코난: 화염의 해바라기', 2015, '애니메이션', '일본어', '시간을 넘어 교착하는 거짓말과 사랑, 인류의 보물을 둘러싼 예술적 미스터리', 0, False]
movie_6 = ['명탐정 코난: 이차원의 저격수', 2014, '애니메이션', '일본어', '밤하늘을 관통하는 정의의 탄환, 그리고 밝혀지는 금단의 수수께끼!', 0, False]
movie_7 = ['명탐정 코난: 11번째 스트라이커', 2012, '애니메이션', '일본어', '의문의 암호는 범인으로부터의 도전장 명탐정을 노리는 함정과 음모에 맞서라', 0, False]
movie_8 = ['명탐정 코난: 침묵의 15분', 2011, '애니메이션', '일본어', '마지막 15분, 예측불허!', 0, False]
movie_9 = ['명탐정 코난: 천공의 난파선', 2010, '애니메이션', '일본어', '괴도 키드 vs 코난 vs 테러리스트, 운명의 삼각대결!', 0, False]

# 2
movies = [movie_1, movie_2, movie_3, movie_4, movie_5, movie_6, movie_7, movie_8, movie_9]

# Define a process
def processes(contains_watched: bool = True):
    # 3
    tag = []
    for movie in movies:
        tag += [[movie[i] for i in range(6)]]

    # 4
    print('*'*40)

    # 5
    for i in range(len(movies)):
        if contains_watched or not movies[i][6]:
            print('{} {}'.format(i+1, movies[i][0]))

    # 6
    print('*'*40)

    # 7
    selects = 0
    while selects not in range(1, 10):
        selects = int(input('Choose a movie number : '))
        if selects not in range(1, 10):
            print('Wrong number')

    # 8
    watch_again = False # Declare variable
    if movies[selects-1][6]:
        watch_again = True if input('You have watched it. Do you like to watch it again? (y) ') is 'y' else False

    # 9
    if watch_again or not movies[selects-1][6]:
        ## A
        print('*'*40)
        ## B
        contents = ['Title', 'Release Date', 'Genres', 'Language', 'Story', 'Likes', 'Watched']
        for i in range(6):
            print('{} : {}'.format(contents[i], movies[selects-1][i]))
        ## C
        print('*'*40)
        ## D / E
        movies[selects-1][6] = True
        if input('Do you like it? (y) ') is 'y':
            new_likes_string = ''
            while not new_likes_string.isdecimal():
                new_likes_string = input('How many likes do you want to add? ')
            movies[selects-1][5] += int(new_likes_string)

    # 10
    print('*'*40)

    # 11
    if input('Next movie (y): ') is not 'y':
        return 0

    # 12
    selects = 0
    while selects not in (1, 2):
        selects = int(input('1. All, 2. Not watched: '))

    # 13 / 14
    return selects

if __name__ == '__main__':
    mode = 1
    while mode:
        mode = processes(True if mode is 1 else False)