from browser import document
from datetime import datetime
from math import pi

def update(canvas, ctx, rad):
    rad *= .9
    draw_base(ctx, rad)
    draw_numbers(ctx, rad)
    draw_time(ctx, rad)

def draw_base(ctx, rad):
    ctx.beginPath()
    ctx.fillStyle = '#FDFDFD'
    ctx.arc(0, 0, rad, 0, 2 * pi)
    ctx.fill()
    ctx.strokeStyle = '#F3F3F3'
    ctx.stroke()
    ctx.strokeStyle = '#000'

def draw_numbers(ctx, rad):
    ctx.font = str(rad * .15) + 'px SpoqaHanSansNeo'
    ctx.textBaseline = 'middle'
    ctx.textAlign = 'center'
    ctx.fillStyle = '#333'
    for i in range(3, 13, 3):
        angle = i * pi / 6
        ctx.rotate(angle)
        ctx.translate(0, -rad * .75)
        ctx.rotate(-angle)
        ctx.fillText(str(i), 0, 0)
        ctx.rotate(angle)
        ctx.translate(0, rad * .75)
        ctx.rotate(-angle)

def draw_time(ctx, rad):
    now = datetime.strptime(document.nowtime, '%Y-%m-%d %H:%M:%S.%f')
    pos = [
        now.hour*pi/6 + now.minute*pi/(6*60) + now.second*pi/(6*60*60),
        now.minute*pi/30 + now.second*pi/(30*60),
        now.second*pi/30
    ]
    draw_hand(ctx, pos[0], rad*.5, rad*.07)
    draw_hand(ctx, pos[1], rad*.8, rad*.07)
    draw_hand(ctx, pos[2], rad*.9, rad*.02)

def draw_hand(ctx, pos, length, width):
    ctx.beginPath()
    ctx.lineWidth = width
    ctx.lineCap = 'round'
    ctx.moveTo(0, 0)
    ctx.rotate(pos)
    ctx.lineTo(0, -length)
    ctx.stroke()
    ctx.rotate(-pos)
    