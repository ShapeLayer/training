print('''맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.
- 햄버거(입력 b)
- 치킨(입력 c)
- 피자(입력 p)
메뉴를 선택하세요(알파벳 b, c, p 입력) : ''', end = '')
while True:
    rec = input()
    if rec == 'b':
        print('햄버거를 선택하였습니다.')
        break
    elif rec == 'c':
        print('치킨을 선택하였습니다.')
        break
    elif rec == 'p':
        print('피자를 선택하였습니다.')
        break
    else:
        print('메뉴를 다시 입력하세요(알파벳 b, c, p 입력) : ', end = '')