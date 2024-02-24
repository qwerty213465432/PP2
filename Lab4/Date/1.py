import datetime

today = datetime.datetime.now()
days_5 = today - datetime.timedelta(days=5)

print(days_5.strftime("%d/%m/%Y, %H:%M:%S"))