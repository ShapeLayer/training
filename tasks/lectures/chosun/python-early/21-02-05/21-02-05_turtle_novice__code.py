import turtle
from sys import argv

# 문제 번호를 실행 인자로 받음
# 예시: python 21-01-31__code_stu.py [문제 번호]
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
    for i in range(3):
        t.forward(100)
        t.left(120)
    t.up()
    t.forward(200)
    t.down()
    for i in range(4):
        t.forward(100)
        t.left(90)

# 2번 문제
elif argv[1] == '2':
    for i in range(6):
        t.forward(100)
        t.left(60)
    t.circle(100)

# 3번 문제
elif argv[1] == '3':
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)

# 4번 문제
elif argv[1] == '4':
    t.width(10)
    t.forward(100)
    t.left(90)
    t.forward(100)

# 5번 문제
elif argv[1] == '5':
    t.color('blue')
    t.forward(100)

# 6번 문제
elif argv[1] == '6':
    t.shape('square')
    t.forward(100)

# 7번 문제
elif argv[1] == '7':
    t.up()
    t.goto(100, 100)
    t.down()
    t.forward(100)
    t.up()
    t.goto(100, 200)
    t.down()
    t.forward(100)

# 8번 문제
elif argv[1] == '8':
    t.circle(50)
    t.up()
    t.goto(-100, 0)
    t.down()
    t.circle(50)
    t.up()
    t.goto(50, 50)
    t.down()
    t.circle(50)
    t.up()
    t.goto(-50, 50)
    t.down()
    t.circle(50)
    t.up()
    t.goto(-150, 50)
    t.down()
    t.circle(50)

# ===== #
t.getscreen()._root.mainloop()