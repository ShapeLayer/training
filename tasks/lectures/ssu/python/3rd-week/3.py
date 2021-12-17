name = input('이름을 입력하세요 : ')
height = float(input('키(m)를 입력하세요. : '))
weight = int(input('몸무게(kg)를 입력하세요 : '))
print('{} 님의 체질량(BMI) 지수는 {} 입니다.'.format(name, round(weight/(height*height),2)))