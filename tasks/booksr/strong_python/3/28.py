is_reverse_integer = True
puts = input('정수를 입력하시오 : ')
int(puts) # 정수가 아닐때 예외를 abort할 수 있도록 처리
for i in range(len(puts)//2 if len(puts)%2==0 else (len(puts)//2)+1):
    if not puts[i] == puts[len(puts)-i-1]:
        is_reverse_integer = False
        break
if is_reverse_integer:
    print('{}은(는) 거꾸로 정수입니다.'.format(puts))
else:
    print('{}은(는) 거꾸로 정수가 아닙니다.'.format(puts))