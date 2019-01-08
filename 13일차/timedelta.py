import datetime
hundred = datetime.timedelta(days=100)
datetime.datetime.now()+hundred
type(datetime.datetime.now())  # <class 'datetime.datetime'>
hundred_before = datetime.timedelta(days=-100)
datetime.datetime.now() + hundred_before
datetime.datetime.now() - hundred
tomorrow = datetime.datetime.now().replace(hour=9, minute=0, second=0) + \
    datetime.timedelta(days=1)

# 실습

hundred = datetime.timedelta(days=100)
hundred_after = datetime.datetime.now().replace(
    hour=9, minute=0, second=0) + datetime.timedelta(days=100)
print("{}/{}/{}  {}:{}:{}".format(hundred_after.year, hundred_after.month,
                                  hundred_after.day, hundred_after.hour, hundred_after.minute, hundred_after.second))
