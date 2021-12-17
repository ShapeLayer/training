print('''맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.
1) 햄버거
2) 치킨
3) 피자
1에서 3까지의 메뉴를 선택하세요 : ''', end = '')
while True:
    rec = int(input())
    if rec == 1:
        print('햄버거를 선택하였습니다.')
        break
    elif rec == 2:
        print('치킨을 선택하였습니다.')
        break
    elif rec == 3:
        print('피자를 선택하였습니다.')
        break
    else:
        print('메뉴를 다시 입력하세요: ', end = '')