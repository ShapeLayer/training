import turtle
from math import floor
from random import choice, randrange

# Configurations
TURTLE_WINDOW_SIZE = 800
LIMITATION = 0

# Init
t = turtle.Turtle()

class Polygon:
    def __init__(self, number: float, length: float, line_width: float) -> None:
        self.number = number
        self.length = length
        self.line_width = line_width

# Q8
def setup() -> str:
    turtle.title('hw3')
    turtle.setup(TURTLE_WINDOW_SIZE, TURTLE_WINDOW_SIZE)
    color = choice(('yellow', 'red', 'violet', 'blue', 'skyblue', 'lightgreen', 'white', 'green', 'brown', 'magenta'))
    turtle.bgcolor(color)
    return color

# Q1~4
def get(q: int) -> float:
    n = 0
    puts = ''
    while True:
        try:
            # Qn-A
            puts = input('Enter the {} of sides for your polygon: '.format('number' if q == 2 else 'length' if q == 3 else 'line width'))
            n = float(puts)
            # Q2-A
            if q == 2:
                n = floor(n)
            break
        # Q2-B / Q3-A / Q4-A
        except ValueError:
            print('SYSTEM ERROR: could not convert string to float: \'{}\''.format(puts))
    # Q2-C
    if q == 2:
        if n < 3:
            raise AssertionError('The input must be 3 or greater.')
        global LIMITATION
        LIMITATION = TURTLE_WINDOW_SIZE / (n/2)
    # Q3-B
    elif q == 3:
        if n < 10 or n > LIMITATION:
            raise AssertionError('The input must be an appropriate number.')
    # Q4-B
    elif q == 4:
        if n <= 0:
            raise AssertionError('The input must be positive.')
    # Q2-D / Q3-C
    print('The confirmed {} of sides for your polygon is {}'.format('number' if q == 2 else 'length' if q == 3 else 'line width', n))
    return n

# Q6
def drawPolygon(sideLength: float, numSides: float, lineWidth: float, bgColor: str) -> None:
    colors = ['yellow', 'red', 'violet', 'blue', 'skyblue', 'lightgreen', 'white', 'green', 'brown', 'magenta']
    colors.remove(bgColor)
    t.color(choice(colors))
    turnAngle = 360 / numSides
    t.pensize(lineWidth)
    t.speed(0) # Q8-A
    # Q8-B
    t.penup()
    t.goto(randrange(-100, 100), randrange(-100, 100))
    for i in range(numSides):
        t.pendown()
        t.forward(sideLength)
        t.right(turnAngle)
    t.penup()

if __name__ == '__main__':
    # Q1
    print('='*50)
    print('Welcome!')
    print('='*50)
    ans=[]
    # Q5
    while True:
        ans += [Polygon(get(q=2), get(q=3), get(q=4))]
        if input('Another Polygon? (y) ') not in ['y', 'Y']:
            break
    # Q7
    bgcolor = setup()
    # Q8
    for i in range(len(ans)):
        polygon = ans[i]
        drawPolygon(polygon.length, polygon.number, polygon.line_width, bgcolor)
        t.write('{} {}'.format(i, t.pos()))
        t.goto(0, 0)
    t.getscreen()._root.mainloop()