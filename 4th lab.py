from datetime import date, timedelta, datetime

# substract 5 days from today's date
print(date.today() - timedelta(5))

# print yesterday, today and tomorrow
print('yesterday %s' % (date.today() - timedelta(1))) #yesterday
print('today %s' % date.today()) #today
print('tomorrow %s' % (date.today() + timedelta(1))) #tomorrow

# drop microseconds from datetime
print(datetime.today().replace(microsecond=0))

# calculate 2 dates difference in seconds
print((datetime.today() - (datetime.today() - timedelta(1))).total_seconds())