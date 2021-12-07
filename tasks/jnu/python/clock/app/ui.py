from browser import document, console, alert
from datetime import date, datetime
from calendar import monthrange
from math import pi

def load_clock_str(type_: str) -> str:
    if type_ not in ['primary', 'secondary', 'primary_sub']:
        raise ValueError('"type_" must be "primary" or "secondary"')
    elif type_ == 'primary':
        return datetime.now().strftime('%H시 %M분')
    elif type_ == 'primary_sub':
        return datetime.now().strftime(':%S')
    elif type_ == 'secondary':
        return datetime.now().strftime('%Y년 %m월 %d일')

def clock_value_handler():
    if not document.nowtime_lock:
        document.nowtime = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S.%f')
    clock_onchange_handler()

def clock_onchange_handler(e = None):
    if e:
        document.nowtime_lock = True
        nowtime = datetime(
            year = int(document['clock-year'].value),
            month = int(document['clock-month'].value),
            day = int(document['clock-day'].value),
            hour = int(document['clock-hour'].value) % 24,
            minute = int(document['clock-min'].value) % 60,
            second = int(document['clock-sec'].value) % 60
        )
        document.nowtime = datetime.strftime(nowtime, '%Y-%m-%d %H:%M:%S.000001')
        document['reset-btn'].disabled = False
    val = datetime.strptime(document.nowtime, '%Y-%m-%d %H:%M:%S.%f')
    update_calendar(val)
    document['clock-year'].value = '{0:04d}'.format(val.year)
    document['clock-month'].value = '{0:02d}'.format(val.month)
    document['clock-day'].value = '{0:02d}'.format(val.day)
    document['clock-hour'].value = '{0:02d}'.format(val.hour)
    document['clock-min'].value = '{0:02d}'.format(val.minute)
    document['clock-sec'].value = '{0:02d}'.format(val.second)

def reset_btn_onclick_handler(e):
    if document.nowtime_lock:
        document.nowtime_lock = False
        document['reset-btn'].disabled = True

def update_calendar(dt: datetime):
    document['cal'].html = '''<table class="cal">
    <tr>
      <th class="is-red">SUN</th><th>MON</th><th>THU</th><th>WED</th><th>THU</th><th>FRI</th><th class="is-blue">SAT</th>
    </tr>
    {}
    </table>'''.format(write_calendar(dt))

def write_calendar(dt: datetime) -> str:
    init_dt = datetime(year=dt.year, month=dt.month, day=1)
    wd_idx, proceed = (init_dt.weekday() + 1) % 7, 0
    mr = monthrange(dt.year, dt.month)
    table_body = ''
    while proceed < wd_idx + mr[1]:
        tr_body = '<tr>{}</tr>'
        tds = ''
        for i in range(7):
            td_body, td_classname = '', ''
            if proceed < wd_idx or proceed > mr[1]:
                pass
            else:
                now = proceed - wd_idx + 1
                td_body = now
                if dt.day == now:
                    td_classname = 'focus'
            tds += '<td class="{}">{}</td>'.format(td_classname, td_body)
            proceed += 1
        tr_body = tr_body.format(tds)
        table_body += tr_body
    return table_body

def draw_base(ctx, rad):
    ctx.translate(rad, rad)
    rad *= .9
    ctx.arc(0, 0, rad, 0, 2 * pi)
    ctx.fillStyle = '#fff'
    ctx.fill()

def draw_numbers (ctx, rad):
    ctx.font = rad * .15 + 'px SpoqaHanSansNeo'
    console.log(2)
    ctx.textBaseline = 'middle'
    console.log(1)
    ctx.textAlign = 'center'
    for i in range(3, 13, 3):
        console.log(True)
        angle = i * pi / 6
        ctx.fillStyle = '#000'
        ctx.rotate(angle)
        ctx.translate(0, -rad * .75)
        ctx.rotate(-angle)
        ctx.fillText(str(i), 0, 0)
        ctx.rotate(angle)
        ctx.translate(0, rad * .75)
        ctx.rotate(-angle)

def draw_hand(ctx, pos, length, width):
    ctx.beginPath()
    ctx.lineWidth = width
    ctx.lineCap = 'round'
    ctx.moveTo(0, 0)
    ctx.rotate(pos)
    ctx.lineTo(0, -length)
    ctx.stroke()
    ctx.rotate(-pos)
