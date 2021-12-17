arr = []
while True:
    t = input('강아지 이름을 입력하시오 : ')
    if t == 'q':
        break
    arr += [t]
print('입력받은 강아지 : ')
print(', '.join(arr))