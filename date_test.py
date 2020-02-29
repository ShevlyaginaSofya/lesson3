from datetime import datetime, timedelta
date_today = datetime.today()
delta = timedelta(days=1)
delta_m = timedelta(days=30)
date_tom = date_today + delta
date_tom_m = date_today + delta_m
print(datetime.today().strftime('%Y-%m-%d'))
print(date_tom.strftime('%Y-%m-%d'))
print(date_tom_m.strftime('%Y-%m-%d'))
date_in = '01.01.17 12:10:03.234567'
print(datetime.strptime(date_in,'%d.%m.%y %H:%M:%S.%f'))
