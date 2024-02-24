import datetime

today = datetime.datetime.now()
yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
tommorow=datetime.datetime.now() + datetime.timedelta(days = 1)

Tod=today.strftime("%A, %B")
Yes=yesterday.strftime("%A, %B")
Tom=tommorow.strftime("%A, %B")


print("Today:", Tod,"\nYesterday:", Yes,"\nTommorow:", Tom)

