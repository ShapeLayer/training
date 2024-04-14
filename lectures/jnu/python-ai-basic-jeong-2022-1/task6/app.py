data = int(input('수심을 입력하세요: '))
converts = 20 - data * (.7/10) # dx/dy = 0.7/10
print(f'수심이 {data}m이면 수온은 {converts}도이다.')
print('수심이 %dm이면 수온은 %.1f도이다.' % (data, converts)) # %.1f = 소수 첫번째 자리까지 표기
print('수심이 {}m이면 수온은 {}도이다.'.format(data, converts))