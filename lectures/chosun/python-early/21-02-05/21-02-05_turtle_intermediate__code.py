from sys import argv
import turtle
from math import cos, pi

# 문제 번호를 실행 인자로 받음
# 예시: python 21-01-31__code_for.py [문제 번호]
# 문제 번호 부분을 공란으로 두면 1번 문제 실행

if len(argv) == 1:
    argv += ['1']

t = turtle.Turtle()
t.shape('turtle')
t.color('black')
t.speed(5)
t.width(1)

# 1번 문제
if argv[1] == '1':
    for i in range(6):
        t.circle(50)
        t.left(60)

# 2번 문제
elif argv[1] == '2':
    for i in range(3):
        t.forward(50)
        t.left(120)
    t.up()
    t.forward(100)
    t.down()
    for i in range(4):
        t.forward(50)
        t.left(90)

# 3번 문제
elif argv[1] == '3':
    n = 0
    while True:
        usr_input = turtle.textinput('Python Turtle Graphics', '몇각형을 원하시나요?')
        try:
            n = int(usr_input)
            if n >= 3:
                break
        except ValueError:
            pass
    ang = 360/n
    for i in range(n):
        t.forward(50)
        t.left(ang)

# 4번 문제
elif argv[1] == '4':
    t.color('red')
    for i in range(12):
        t.up()
        t.forward(50)
        t.down()
        t.forward(50)
        t.up()
        t.forward(25)
        t.stamp()
        t.goto(0, 0)
        t.left(30)
        
# 5번 문제
elif argv[1] == '5':
    t.left(90)
    for i in range(6):
        t.forward(100)
        t.forward(-30)
        t.left(60)
        t.forward(30)
        t.forward(-30)
        t.right(120)
        t.forward(30)
        t.forward(-30)
        t.up()
        t.goto(0, 0)
        t.down()

# 6번 문제
elif argv[1] == '6':
    t.speed(10)
    t.shape('arrow')
    t.color('red')
    # 정오각별을 한붓그리기 했을때 별 내부의 정오각형을 기준으로 상수 설정
    # n :   정오각형의 한 변
    # l :   한붓그리기 시 다음 회전까지 Turtle이 지나가야 하는 거리
    #       식: n + (n/2) * sec(π/5) * 2
    n = 100
    l = n * (1+(cos(0.2*pi)**-1))
    while True:
        for i in range(5):
            t.forward(l)
            # 정오각별의 꼭지각이 36도이므로 144도 우측 회전
            t.right(144)
        t.left(10)

# 7번 문제
elif argv[1] == '7':
    while True:
        t.forward(200)
        t.right(90)
        t.forward(15)
        t.right(90)
        t.forward(200)
        t.left(90)
        t.forward(15)
        t.left(90)


# ===== #
t.getscreen()._root.mainloop()