sleep_time = 0
while True:
    sleep_time_raw = input('어제 몇 시간 주무셨나요? ')
    try:
        sleep_time = float(sleep_time_raw)
        print('수면 시간은 {}, 참'.format(sleep_time))
        break
    except ValueError:
        print('수면 시간은 {}, 거짓'.format(sleep_time_raw))

walk_count = int(input('어제 얼마나 걸었나요? '))

comment = input('6자 이상의 파이팅 문구를 입력해주세요: ')
if len(comment) < 6:
    print('6자 미만의 문구를 입력하셨습니다..')

if sleep_time == 0:
    cause = input('왜 어제밤 못 주무셨나요? ')
    if cause in ['숙제', '시험', '스트레스']:
        print('마음이 편안해지는 음악을 추천해드려요: Physical Emotion (https://www.youtube.com/watch?v=UEl-5wwNA6o)')
    elif cause == '불면':
        print('잠이 잘 오는 음악을 추천해드려요: [대성마이맥]수학 한석원 - 2018년 6월 모의평가 해설 수학 가형 (https://www.youtube.com/watch?v=goYGMjo13-k)')

walk_count_per_awake = int(walk_count / (24 - sleep_time))
if sleep_time <= 6 and walk_count <= 8000:
    print(''.join([comment[i] if i == 0 or i == len(comment)-1 else '+' for i in range(len(comment))]))
elif sleep_time <= 6:
    star_display = ''.join(['*' for i in range(int(sleep_time))])
    print('{} 오늘은 꼭 {}시간 잠을 주무세요 {}'.format(star_display, sleep_time, star_display))
elif sleep_time > 6 and sleep_time < 9:
    print('오늘 매 시간 당 {} 걸음을 걸으셨습니다.'.format(walk_count_per_awake))
    print('건강하게 잘 지내고 계시네요! 앞으로도 이렇게만 생활하세요.')
elif sleep_time >= 9:
    favorite_num = int(input('2에서 9 사이의 숫자 중에서 좋아하는 숫자 하나를 입력해주세요: '))
    if walk_count >= 8000:
        if walk_count_per_awake >= 1000:
            if 0 in [favorite_num % 2, favorite_num % 3]:
                if favorite_num % 2 == 0 and favorite_num % 3 == 0:
                    print(comment)
                else:
                    print(comment[:favorite_num])
        else:
            print('오늘은 {}시간 깨어계셨고, 매 시간 당 {}걸음 걸으셨습니다.'.format((24 - sleep_time), walk_count_per_awake))
    else:
        print(''.join([str(favorite_num) for _ in range(len(comment))]))
