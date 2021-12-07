from browser import document, console, alert
from datetime import date, datetime
from calendar import monthrange
from math import pi

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
