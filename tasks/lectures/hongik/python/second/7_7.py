# python 7_7.py [문제 번호]
# 예: python 7_7.py 3

import turtle
from math import log, sin, cos, radians
from sys import argv

def draw_axis():
    size = 400
    t.goto(-1*size, 0)
    t.down()
    t.forward(size*2)
    t.up()
    t.goto(0, -1*size)
    t.down()
    t.left(90)
    t.forward(size*2)
    t.up()
    t.goto(0, 0)

## Init
t = turtle.Turtle()
t.up()
multiple = [1, 1]
limit = 0
if argv[1] == '1':
    x, y, inter = -29, 0, 30
elif argv[1] == '2' or argv[1] == '3':
    limit = 360
    x, y, inter = -4, 0, 5
    draw_axis()
    if argv[1] == '3':
        multiple = [1, 10]
elif argv[1] == '4':
    draw_axis()
    print(True)
    multiple = [0, 100]
t.goto(0, 0)
t.down()

## Main
if argv[1] != '4':
    while True:
        if limit and x > limit:
            break
        x += inter
        y = log(x)
        print(x, y)
        t.goto(x*multiple[0], y*multiple[1])
else:
    for i in range(2):
        t.up()
        t.goto(-360, i*100)
        t.down()
        if not i:
            t.color('red')
        else:
            t.color('blue')
        for j in range(-360, 360):
            if not i:
                y = sin(radians(j)) * multiple[1]
            else:
                y = cos(radians(j)) * multiple[1]
            t.goto(j, y)


t.getscreen()._root.mainloop()