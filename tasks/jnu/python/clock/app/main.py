from browser import document, timer
from datetime import datetime
from app.ui import update_calendar, clock_onchange_handler, clock_value_handler, reset_btn_onclick_handler
from app.analog_clock import update

update_calendar(datetime.now())

# Digital Clock
document.nowtime_lock = False
timer.set_interval(clock_value_handler, 1800)
document['clock'].bind('change', clock_onchange_handler)
document['reset-btn'].bind('click', reset_btn_onclick_handler)

# Analog Clock
canvas = document['analog-clock']
ctx = canvas.getContext('2d')
rad = canvas.height / 2
ctx.translate(rad, rad)
timer.set_interval(lambda: update(canvas, ctx, rad), 100)
