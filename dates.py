import datetime

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.time())

d = datetime.datetime(2020,1,1)

yesterday = now - datetime.timedelta(1)
print(yesterday)

# String Formatting
# https://www.w3schools.com/python/python_datetime.asp
print(now.strftime("%A, %B %d, %Y"))