import datetime

# Task-1

todie = datetime.datetime.now() - datetime.timedelta(days=5)
print(todie)

# Task-2

print(datetime.datetime.now() - datetime.timedelta(days=1))
print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(days=1))

# Task-3

print(datetime.datetime.now().replace(microsecond=0))

# Task-4

date1 = datetime.datetime.now()
date2 = datetime.datetime(2026, 7, 26)

diff = date2 - date1

print(diff.total_seconds())
