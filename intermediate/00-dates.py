# Dates

# Modulo donde estan representados todos los objetos y funciones relacionadas con las fechas
# No es un objeto basico, es complejo, por eso esta representado en un modulo
from datetime import datetime, time, date, timedelta

# creamos una fecha que sea la representacion de la fecha ahora
now_date = datetime.now()
now_date_timestamp = now_date.timestamp()


def print_date(date):
  print('year:',date.year)
  print('month:',date.month)
  print('day:',date.day)
  print('hour:',date.hour)
  print('minute:',date.minute)
  print('second:',date.second)
  print('timestamp:',date.timestamp())

print_date(now_date)

year_2025 = datetime(2025, 1, 1, 23)
print_date(year_2025)

# vamos a practicar con el tiempo.
now_time = time(23, 18, 28)

print(now_time.hour)
print(now_time.minute)
print(now_time.second)

# vamos a practicar con date
now_date = date(2024, 5, 3)
print(now_date.year)
print(now_date.month)
print(now_date.day)

# diferencia 
date1 = datetime(2023,1,1)
date2 = datetime(2023,5,1)

# time1 = time(22,15,35)
# time2 = time(23,15,35)

diff_date = date2 - date1
# diff_time = time2 - time1

print('diff_date',diff_date)
# print('diff_time',diff_time)

# timedelta sirve para operar y tabajar con diferencias de fechas
# trabajar con franjas de fechas
# Representa la diferencia entre dos objetos datetime
start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print('start timedelta',start_timedelta)
print('end timedelta',end_timedelta)
print('end - start',end_timedelta - start_timedelta)
print('end + start',end_timedelta + start_timedelta)