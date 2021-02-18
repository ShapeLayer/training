from datetime import datetime, timezone, timedelta

kst = timezone(timedelta(hours=9))
print(datetime.now(kst).strftime('%Y-%m-%d'))